"""
A tiny REST API used as the 'application under test' for the
API testing and Performance testing tool demos (Postman / JMeter category).
Run: python3 src/api_server.py
"""
from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/health":
            self._send_json(200, {"status": "ok"})
        elif self.path.startswith("/add"):
            from urllib.parse import urlparse, parse_qs
            qs = parse_qs(urlparse(self.path).query)
            try:
                a = float(qs.get("a", [0])[0])
                b = float(qs.get("b", [0])[0])
                self._send_json(200, {"result": a + b})
            except (ValueError, IndexError):
                self._send_json(400, {"error": "invalid parameters"})
        else:
            self._send_json(404, {"error": "not found"})

    def _send_json(self, code, payload):
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(payload).encode())

    def log_message(self, format, *args):
        pass  # keep console clean


if __name__ == "__main__":
    print("API server running at http://127.0.0.1:8899")
    HTTPServer(("127.0.0.1", 8899), Handler).serve_forever()
