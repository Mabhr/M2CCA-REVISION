#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
sync_data.py — Synchronise le bloc FALLBACK de chaque page de cours
avec son fichier de données data/<cours>.json.

Le fichier data/<cours>.json est la SOURCE UNIQUE de vérité.
Le bloc « const FALLBACK = {...}; » présent dans chaque <cours>.html
n'est qu'une copie de secours utilisée quand la page est ouverte en
local (protocole file://), où la requête fetch() échoue.

Sans cet outil, les deux peuvent diverger : la page servie par un
serveur montre data/<cours>.json à jour, mais la même page ouverte
directement affiche un FALLBACK périmé.

Usage :  python3 tools/sync_data.py
À relancer après chaque modification d'un fichier data/<cours>.json.
"""

import io, json, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
COURSES = ["conduite_chgt", "evo_orga", "gouv", "inge_fi", "rse", "strat"]


def find_json_end(s, start):
    """Renvoie l'index juste après l'accolade fermante de l'objet JSON
    qui commence à s[start] == '{', en respectant les chaînes."""
    depth = 0
    in_str = False
    esc = False
    i = start
    while i < len(s):
        c = s[i]
        if in_str:
            if esc:
                esc = False
            elif c == '\\':
                esc = True
            elif c == '"':
                in_str = False
        else:
            if c == '"':
                in_str = True
            elif c == '{':
                depth += 1
            elif c == '}':
                depth -= 1
                if depth == 0:
                    return i + 1
        i += 1
    return -1


def sync_one(course):
    html_path = os.path.join(ROOT, course + ".html")
    json_path = os.path.join(ROOT, "data", course + ".json")
    if not os.path.exists(html_path) or not os.path.exists(json_path):
        return (course, "ignoré (fichier manquant)")

    data = json.load(io.open(json_path, encoding="utf-8"))
    html = io.open(html_path, encoding="utf-8").read()

    kw = "const FALLBACK = "
    k = html.find(kw)
    if k == -1:
        return (course, "ignoré (FALLBACK introuvable)")
    brace = html.find("{", k)
    end = find_json_end(html, brace)
    if end == -1:
        return (course, "ERREUR (objet FALLBACK mal formé)")

    new_block = kw + json.dumps(data, ensure_ascii=False, indent=2)
    if html[k:end] == new_block:
        return (course, "déjà à jour")

    new_html = html[:k] + new_block + html[end:]
    io.open(html_path, "w", encoding="utf-8").write(new_html)
    return (course, "synchronisé")


def main():
    print("Synchronisation FALLBACK <- data/*.json\n")
    err = False
    for c in COURSES:
        name, status = sync_one(c)
        print("  %-16s %s" % (name, status))
        if status.startswith("ERREUR"):
            err = True
    print("\nTerminé." + ("  (avec erreurs)" if err else ""))
    sys.exit(1 if err else 0)


if __name__ == "__main__":
    main()
