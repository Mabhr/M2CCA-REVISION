"""Tagge le champ 'src' sur les flashcards et quiz selon le contenu.

Stratégie : pour chaque card, on infère la source du PDF prof en cherchant des mots-clés
spécifiques dans le contenu. Si reconnu → ajoute src; sinon laisse vide (signe d'alerte).
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / 'data'

# Règles : keyword (lowercase) → source string
# Format source : "Auteur — Cours p.X" ou "Cours — Auteur".
# L'ordre compte : keywords spécifiques d'abord, génériques après.

CONDUITE_RULES = [
    # PDF GESTION DES COMPETENCES (p.3-41)
    ("rôle confié", "Besombes — Compétences p.3"),
    ("rôle perçu", "Besombes — Compétences p.3"),
    ("compétence est une disposition", "Besombes — Compétences p.6"),
    ("savoir, savoir-faire", "Besombes — Compétences p.6"),
    ("gpec", "Besombes — Compétences p.11"),
    ("éthique de performance", "Besombes — Compétences p.12"),
    ("organisation qualifiante", "Besombes — Compétences p.14"),
    ("description de poste", "Besombes — Compétences p.18-19"),
    ("dictionnaire de compétences", "Besombes — Compétences p.15"),
    ("intitulé du poste", "Besombes — Compétences p.19"),
    ("3 dimensions des compétences", "Besombes — Compétences p.20"),
    ("évaluation sanction", "Besombes — Compétences p.25"),
    ("formative", "Besombes — Compétences p.25"),
    ("missionnement", "Besombes — Compétences p.27"),
    ("3 types d'appréciation", "Besombes — Compétences p.27"),
    ("mythes", "Besombes — Compétences p.30"),
    ("rites", "Besombes — Compétences p.30"),
    ("5 étapes de constitution d'une équipe", "Besombes — Compétences p.31-32"),
    ("interdépendance", "Besombes — Compétences p.33"),
    ("continuum", "Besombes — Compétences p.35"),
    ("cap", "Besombes — Compétences p.36"),
    ("4 attentes", "Besombes — Compétences p.37"),
    ("agilité managériale", "Besombes — Compétences p.38"),
    ("gilbert (1980)", "Besombes — Compétences p.40"),
    ("gilbert 1980", "Besombes — Compétences p.40"),
    # PDF CONDUITE DU CHANGEMENT (p.1-47)
    ("le chatelier", "Besombes — Conduite p.3"),
    ("kurt lewin", "Besombes — Conduite p.5"),
    ("décristallisation", "Besombes — Conduite p.5"),
    ("kübler-ross", "Besombes — Conduite p.6"),
    ("facteurs psychosociologiques", "Besombes — Conduite p.7"),
    ("résistance", "Besombes — Conduite p.8-9"),
    ("coercition", "Besombes — Conduite p.10"),
    ("persuasion rationnelle", "Besombes — Conduite p.10"),
    ("partage de pouvoir", "Besombes — Conduite p.10"),
    ("partage du pouvoir", "Besombes — Conduite p.10"),
    ("univers du changement", "Besombes — Conduite p.12"),
    ("8 étapes", "Besombes — Conduite p.13-23"),
    ("amorcer", "Besombes — Conduite p.15"),
    ("comité de pilotage", "Besombes — Conduite p.14"),
    ("vocation", "Besombes — Conduite p.27-30"),
    ("écouter, mobiliser", "Besombes — Conduite p.27"),
    ("gains attendus", "Besombes — Conduite p.31"),
    ("matrice importance", "Besombes — Conduite p.32"),
    ("proactifs", "Besombes — Conduite p.36"),
    ("passifs", "Besombes — Conduite p.36"),
    ("opposants", "Besombes — Conduite p.36"),
    ("ressources métiers", "Besombes — Conduite p.39"),
    ("raci", "Besombes — Conduite p.40"),
    ("pourquoi changer", "Besombes — Conduite p.41"),
    ("instance décisionnaire", "Besombes — Conduite p.42"),
    ("10 points clés", "Besombes — Conduite p.46-47"),
]

EVO_RULES = [
    ("400 000", "Besombes — Évo p.3-5"),
    ("3 logiques", "Besombes — Évo p.5"),
    ("logique de production", "Besombes — Évo p.5"),
    ("logique de vente", "Besombes — Évo p.5"),
    ("création de valeur", "Besombes — Évo p.5"),
    ("entreprises virtuelles", "Besombes — Évo p.6"),
    ("fabless", "Besombes — Évo p.6"),
    ("besoin → organisation", "Besombes — Évo p.7"),
    ("bor", "Besombes — Évo p.7"),
    ("12 thèmes", "Besombes — Évo p.8"),
    ("drucker", "Besombes — Évo p.10-12 (DPPO)"),
    ("dppo", "Besombes — Évo p.10-12"),
    ("différenciation", "Besombes — Évo p.13"),
    ("le métier", "Besombes — Évo p.14"),
    ("savoir-faire", "Besombes — Évo p.14"),
    ("tainter", "Besombes — Évo p.15-16"),
    ("effondrement", "Besombes — Évo p.15-16"),
    ("deloitte", "Besombes — Évo p.17"),
    ("philippe burger", "Besombes — Évo p.17"),
    ("réseau d'équipes", "Besombes — Évo p.17"),
    ("culture", "Besombes — Évo p.19"),
    ("paul valéry", "Besombes — Évo p.20"),
    ("approche processus", "Besombes — Évo p.21-32"),
    ("iso 8402", "Besombes — Évo p.28"),
    ("iso 9001", "Besombes — Évo p.27"),
    ("réalisation", "Besombes — Évo p.25"),
    ("macroprocessus", "Besombes — Évo p.26"),
    ("tortue de crosby", "Besombes — Évo p.29"),
    ("avec quoi", "Besombes — Évo p.29"),
    ("cartographie", "Besombes — Évo p.30"),
    ("chandler", "Besombes — Évo p.34"),
    ("edgar morin", "Besombes — Évo p.34"),
    ("ago-antagoniste", "Besombes — Évo p.34"),
    ("us navy", "Besombes — Évo p.38"),
    ("efficacité vs efficience", "Besombes — Évo p.39"),
    ("modèle de gilbert", "Besombes — Évo p.41"),
    ("crozier", "Besombes — Évo p.42"),
    ("analyse stratégique", "Besombes — Évo p.42"),
    ("corps vivant", "Besombes — Évo p.42"),
    ("pouvoir, droit, intérêt", "Besombes — Évo p.43"),
    ("pouvoir / droit / intérêt", "Besombes — Évo p.43"),
    ("ghosn", "Besombes — Évo p.44"),
    ("5 % de stratégie", "Besombes — Évo p.44"),
    ("dialogue social", "Besombes — Évo p.44"),
    ("structure fonctionnelle", "Besombes — Évo p.45"),
    ("structure projet", "Besombes — Évo p.45"),
    ("pdca", "Besombes — Évo p.45"),
    ("7 leviers", "Besombes — Évo p.46"),
    ("karajan", "Besombes — Évo p.50"),
    ("co-construire", "Besombes — Évo p.54"),
    ("co-agir", "Besombes — Évo p.54"),
]

RSE_RULES = [
    ("4 piliers", "Duheron — RSE + ESRS xlsx"),
    ("gov / sbm / iro", "Duheron — RSE + ESRS xlsx"),
    ("82 disclosure", "ESRS xlsx checklist"),
    ("dr esrs 2", "ESRS xlsx checklist"),
    ("e1-9", "ESRS xlsx checklist"),
    ("charge de la preuve inversée", "ESRS xlsx checklist"),
    ("phase-ins", "ESRS xlsx checklist"),
    ("rapport draghi", "Omnibus.docx"),
    ("omnibus", "Omnibus.docx"),
    ("green asset ratio", "Omnibus.docx"),
    ("johannesburg", "Duheron — RSE"),
    ("3 piliers du développement", "Duheron — RSE"),
    ("global compact", "Duheron — RSE"),
    ("kofi annan", "Duheron — RSE"),
    ("matrice de matérialité", "Duheron — RSE"),
    ("iro", "Duheron — RSE + ESRS xlsx"),
    ("impacts, risques et opportunités", "Duheron — RSE + ESRS xlsx"),
    ("cs3d", "Omnibus.docx"),
    ("devoir de vigilance", "Omnibus.docx"),
    ("csrd", "Duheron — RSE / Omnibus.docx"),
    ("12 esrs", "Duheron — RSE"),
    ("double matérialité", "Duheron — RSE"),
    ("vsme", "Duheron — RSE"),
    ("société à mission", "Duheron — RSE"),
    ("loi pacte", "Duheron — RSE"),
    ("greenwashing", "Duheron — RSE"),
    ("donut", "Duheron — RSE (Raworth 2010)"),
    ("raworth", "Duheron — RSE (Raworth 2010)"),
    ("green deal", "Duheron — RSE"),
]

INGE_FI_RULES = [
    # Robin REDESIGN (cours principal)
    ("cmpc", "Robin — Chap 1 (Coût du capital)"),
    ("rcp", "Robin — Chap 1"),
    ("medaf", "Robin — Chap 1"),
    ("gordon-shapiro", "Robin — Chap 1"),
    ("bêta endetté", "Robin — Chap 1"),
    ("bêta désendetté", "Robin — Chap 1"),
    ("hamada", "Robin — Chap 1"),
    ("βa", "Robin — Chap 1"),
    ("prime d'illiquidité", "Robin — Chap 1"),
    # Marchés
    ("neu cp", "Robin — Chap 2 (Marché monétaire)"),
    ("intérêts pré-comptés", "Robin — Chap 2"),
    ("intérêts post-comptés", "Robin — Chap 2"),
    ("ipo", "Robin — Chap 2 (IPO)"),
    ("opo", "Robin — Chap 2"),
    ("opf", "Robin — Chap 2"),
    ("placement garanti", "Robin — Chap 2"),
    ("opm", "Robin — Chap 2"),
    ("euronext", "Robin — Chap 2"),
    ("amf", "Robin — Chap 2"),
    ("lch clearnet", "Robin — Chap 2"),
    ("appel de marge", "Robin — Chap 2"),
    ("dépôt de garantie", "Robin — Chap 2"),
    ("fixing", "Robin — Chap 2"),
    # Obligations
    ("annuités constantes", "Robin — Chap 3 (Obligations)"),
    ("amortissement constant", "Robin — Chap 3"),
    ("in fine", "Robin — Chap 3"),
    ("coupon couru", "Robin — Chap 3"),
    ("duration", "Robin — Chap 3"),
    ("taux actuariel", "Robin — Chap 3"),
    # Dérivés
    ("fra", "Robin — Chap 5 (Dérivés)"),
    ("forward/forward", "Robin — Chap 5"),
    ("forward forward", "Robin — Chap 5"),
    ("swap", "Robin — Chap 5"),
    ("cap", "Robin — Chap 5"),
    ("floor", "Robin — Chap 5"),
    ("collar", "Robin — Chap 5"),
    # Options
    ("call", "Robin — Chap 6 (Options)"),
    ("put", "Robin — Chap 6"),
    ("américaine vs européenne", "Robin — Chap 6"),
    ("américaine", "Robin — Chap 6"),
    ("européenne", "Robin — Chap 6"),
    ("valeur intrinsèque", "Robin — Chap 6"),
    ("option de change", "Robin — Chap 6"),
    # ESG
    ("donut", "Robin — Chap 7 (ESG, Raworth)"),
    ("raworth", "Robin — Chap 7 (Raworth 2010)"),
    ("scope 1", "Robin — Chap 7 (Bilan Carbone)"),
    ("scope 2", "Robin — Chap 7 (Bilan Carbone)"),
    ("scope 3", "Robin — Chap 7 (Bilan Carbone)"),
    ("12 esrs", "Robin — Chap 7"),
    ("ghg protocol", "Robin — Chap 7"),
    ("omnibus", "Robin — Omnibus.docx"),
    ("csrd", "Robin — Chap 7"),
    ("esrs", "Robin — Chap 7"),
    ("rse", "Robin — Chap 7"),
    ("brundtland", "Robin — Chap 7"),
    ("grenelle", "Robin — Chap 7"),
    ("nfrd", "Robin — Chap 7"),
    ("loi pacte", "Robin — Chap 7"),
]

STRAT_RULES = [
    ("chandler", "Tellier — Intro"),
    ("strategor", "Tellier — Intro"),
    ("plateforme", "Tellier — P1 (Plateformes)"),
    ("benavent", "Tellier — P1 (Benavent 2016)"),
    ("cusumano", "Tellier — P1 (Cusumano 2022)"),
    ("metcalfe", "Tellier — P1"),
    ("longue traîne", "Tellier — P1"),
    ("crowdsourcing", "Tellier — P1"),
    ("appariement", "Tellier — P1"),
    ("marché biface", "Tellier — P1"),
    ("multiface", "Tellier — P1"),
    ("business model", "Tellier — P1"),
    ("osterwalder", "Tellier — P1"),
    ("nespresso", "Tellier — P1"),
    ("tarkett", "Tellier — Intro"),
    ("michelin", "Tellier — Intro"),
    ("5 forces", "Tellier — P2 (Porter 1985)"),
    ("écosystème d'affaires", "Tellier — P2"),
    ("koenig", "Tellier — P2 (Koenig 2004)"),
    ("baumard", "Tellier — P2 (Baumard 2000)"),
    ("bonduelle", "Tellier — P2"),
    ("hermès", "Tellier — P2 (Hermès vs LVMH)"),
    ("gillette", "Tellier — P2 (Gillette vs Bic)"),
    ("alliance", "Tellier — P2"),
    ("entente", "Tellier — P2"),
    ("cartel", "Tellier — P2"),
    ("johnson", "Tellier — P3 (Johnson 2005)"),
    ("matrice pouvoir", "Tellier — P3"),
    ("bcg", "Tellier — P3"),
    ("macs", "Tellier — P3"),
    ("avantage parental", "Tellier — P3"),
    ("parental advantage", "Tellier — P3"),
    ("unilever", "Tellier — P3"),
    ("afep-medef", "Tellier — P3"),
    ("friedman", "Tellier — P3 (Friedman 1970)"),
    ("fonds de pension", "Tellier — P3"),
    ("calpers", "Tellier — P3"),
    ("gouvernance familiale", "Tellier — P3"),
    ("gouvernance actionnariale", "Tellier — P3"),
    ("eads", "Tellier — P3"),
]

GOUV_RULES = [
    ("isaca", "Lebey — Gouvernance"),
    ("cobit", "Lebey — Gouvernance"),
    ("itil", "Lebey — Gouvernance"),
    ("cmmi", "Lebey — Gouvernance"),
    ("coso", "Lebey — Gouvernance"),
    ("val it", "Lebey — Gouvernance"),
    ("risk it", "Lebey — Gouvernance"),
    ("balanced scorecard", "Lebey — Gouvernance"),
    ("henderson-venkatraman", "Lebey — Gouvernance"),
    ("dsi", "Lebey — Gouvernance"),
    ("tma", "Lebey — Gouvernance"),
    ("infogérance", "Lebey — Gouvernance"),
    ("sla", "Lebey — Gouvernance"),
    ("ola", "Lebey — Gouvernance"),
    ("réversibilité", "Lebey — Gouvernance"),
    ("offshore", "Lebey — Gouvernance"),
    ("nearshore", "Lebey — Gouvernance"),
    ("sox", "Lebey — Gouvernance"),
    ("nre", "Lebey — Gouvernance"),
    ("lsf", "Lebey — Gouvernance"),
    ("byod", "Lebey — Gouvernance"),
    ("rgpd", "Sujet UE 7 — M2 CCA 2024-25"),
    ("dpo", "Sujet UE 7 — M2 CCA 2024-25"),
    ("dématérialisation", "Sujet UE 7 — M2 CCA 2024-25"),
    ("coffre-fort", "Sujet UE 7 — M2 CCA 2024-25"),
    ("facturation électronique", "Sujet UE 7 — M2 CCA 2024-25"),
    ("pdp", "Sujet UE 7 — M2 CCA 2024-25"),
    ("ppf", "Sujet UE 7 — M2 CCA 2024-25"),
    ("factur-x", "Sujet UE 7 — M2 CCA 2024-25"),
    ("intelligence artificielle", "Sujet UE 7 — M2 CCA 2024-25"),
    ("ia act", "Sujet UE 7 — M2 CCA 2024-25"),
    ("audit", "Lebey — Audit"),
    ("nep 315", "Lebey — Audit"),
    ("nep 330", "Lebey — Audit"),
    ("pssi", "Lebey — Audit"),
    ("pca", "Lebey — Audit"),
    ("iso 27", "Lebey — Audit/Gouv"),
    ("iso 9001", "Lebey — Gouvernance"),
    ("ebios", "Sujet UE 7 — M2 CCA 2024-25"),
    ("marion", "Sujet UE 7 — M2 CCA 2024-25"),
]

COURSE_RULES = {
    'conduite_chgt': CONDUITE_RULES,
    'evo_orga': EVO_RULES,
    'rse': RSE_RULES,
    'inge_fi': INGE_FI_RULES,
    'strat': STRAT_RULES,
    'gouv': GOUV_RULES,
}


def infer_src(text, rules):
    t = text.lower()
    for kw, src in rules:
        if kw in t:
            return src
    return None


def tag(course):
    path = DATA / f'{course}.json'
    d = json.loads(path.read_text())
    rules = COURSE_RULES.get(course, [])
    if not rules:
        return
    fc_tagged = 0
    for fc in d.get('flashcards', []):
        if fc.get('src'):
            continue
        text = fc.get('q', '') + ' ' + fc.get('a', '')
        s = infer_src(text, rules)
        if s:
            fc['src'] = s
            fc_tagged += 1
    q_tagged = 0
    for q in d.get('quizQuestions', []):
        if q.get('src'):
            continue
        text = q.get('q', '') + ' ' + q.get('e', '')
        s = infer_src(text, rules)
        if s:
            q['src'] = s
            q_tagged += 1
    path.write_text(json.dumps(d, ensure_ascii=False, indent=2))
    total_fc = len(d.get('flashcards', []))
    total_q = len(d.get('quizQuestions', []))
    fc_with_src = sum(1 for fc in d['flashcards'] if fc.get('src'))
    q_with_src = sum(1 for q in d['quizQuestions'] if q.get('src'))
    print(f'{course}:')
    print(f'   flashcards : {fc_with_src}/{total_fc} taguées ({fc_tagged} ajoutées cette passe)')
    print(f'   quiz       : {q_with_src}/{total_q} taggués ({q_tagged} ajoutés cette passe)')


if __name__ == '__main__':
    for c in COURSE_RULES:
        tag(c)
