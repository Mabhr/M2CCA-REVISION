#!/usr/bin/env python3
import os, sys, http.server, socketserver
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
os.chdir(ROOT)
PORT = int(os.environ.get('PORT', '8765'))
class H(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store')
        super().end_headers()
with socketserver.TCPServer(('127.0.0.1', PORT), H) as httpd:
    print(f'serving {ROOT} on http://127.0.0.1:{PORT}')
    httpd.serve_forever()
