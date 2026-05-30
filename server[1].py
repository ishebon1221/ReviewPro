#!/usr/bin/env python3
"""
ReviewPro - خادم Proxy بسيط
يحل مشكلة CORS لـ Google Maps و Anthropic APIs
تشغيل: python3 server.py
"""

import http.server
import urllib.request
import urllib.error
import json
import os

PORT = 8765

class ProxyHandler(http.server.BaseHTTPRequestHandler):

    def log_message(self, format, *args):
        print(f"[{self.path}] {format % args}")

    def send_cors(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "*")

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_cors()
        self.end_headers()

    def do_GET(self):
        # Serve the HTML app
        if self.path == "/" or self.path == "/index.html":
            self.serve_file("reviewpro-final.html", "text/html; charset=utf-8")
        # Resolve short Google Maps URLs to get Place ID
        elif self.path.startswith("/proxy/resolve?url="):
            import urllib.parse
            short_url = urllib.parse.unquote(self.path.split("?url=")[1])
            try:
                req = urllib.request.Request(short_url, method="GET")
                req.add_header("User-Agent", "Mozilla/5.0")
                # Follow redirects and return final URL
                with urllib.request.urlopen(req, timeout=10) as resp:
                    final_url = resp.url
                self.send_response(200)
                self.send_cors()
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps({"url": final_url}).encode())
            except Exception as e:
                self.send_response(500)
                self.send_cors()
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps({"error": str(e)}).encode())
        else:
            self.send_error(404)

    def do_POST(self):
        length = int(self.headers.get("Content-Length", 0))
        body = self.read_body(length)

        # ── Anthropic proxy ──
        if self.path == "/proxy/anthropic":
            self.proxy_request(
                url="https://api.anthropic.com/v1/messages",
                body=body,
                extra_headers={
                    "x-api-key": self.headers.get("x-api-key", ""),
                    "anthropic-version": "2023-06-01",
                    "anthropic-dangerous-direct-browser-access": "true",
                }
            )

        # ── Google Places Text Search ──
        elif self.path == "/proxy/google/search":
            self.proxy_request(
                url="https://places.googleapis.com/v1/places:searchText",
                body=body,
                extra_headers={
                    "X-Goog-Api-Key": self.headers.get("x-goog-api-key", ""),
                    "X-Goog-FieldMask": self.headers.get("x-goog-fieldmask", "*"),
                }
            )

        # ── Google Place Details ──
        elif self.path.startswith("/proxy/google/details/"):
            place_id = self.path.split("/proxy/google/details/")[1]
            self.proxy_get(
                url=f"https://places.googleapis.com/v1/{place_id}",
                extra_headers={
                    "X-Goog-Api-Key": self.headers.get("x-goog-api-key", ""),
                    "X-Goog-FieldMask": "id,displayName,rating,userRatingCount,reviews,formattedAddress",
                }
            )

        else:
            self.send_error(404)

    def read_body(self, length):
        if length > 0:
            return self.rfile.read(length)
        return b""

    def proxy_request(self, url, body, extra_headers={}):
        try:
            req = urllib.request.Request(url, data=body, method="POST")
            req.add_header("Content-Type", "application/json")
            for k, v in extra_headers.items():
                if v:
                    req.add_header(k, v)
            with urllib.request.urlopen(req, timeout=30) as resp:
                data = resp.read()
                self.send_response(200)
                self.send_cors()
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(data)
        except urllib.error.HTTPError as e:
            data = e.read()
            self.send_response(e.code)
            self.send_cors()
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(data)
        except Exception as e:
            self.send_response(500)
            self.send_cors()
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"error": str(e)}).encode())

    def proxy_get(self, url, extra_headers={}):
        try:
            req = urllib.request.Request(url, method="GET")
            for k, v in extra_headers.items():
                if v:
                    req.add_header(k, v)
            with urllib.request.urlopen(req, timeout=30) as resp:
                data = resp.read()
                self.send_response(200)
                self.send_cors()
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(data)
        except Exception as e:
            self.send_response(500)
            self.send_cors()
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"error": str(e)}).encode())

    def serve_file(self, filename, content_type):
        filepath = os.path.join(os.path.dirname(__file__), filename)
        try:
            with open(filepath, "rb") as f:
                data = f.read()
            self.send_response(200)
            self.send_header("Content-Type", content_type)
            self.send_header("Content-Length", str(len(data)))
            self.end_headers()
            self.wfile.write(data)
        except FileNotFoundError:
            self.send_error(404, f"File not found: {filename}")


if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    server = http.server.HTTPServer(("localhost", PORT), ProxyHandler)
    print(f"""
╔══════════════════════════════════════╗
║      ReviewPro Server - جاهز        ║
╠══════════════════════════════════════╣
║  افتح المتصفح على:                  ║
║  http://localhost:{PORT}               ║
╚══════════════════════════════════════╝
اضغط Ctrl+C للإيقاف
""")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nتم إيقاف الخادم.")
