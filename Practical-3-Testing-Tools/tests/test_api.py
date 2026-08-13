"""
API Testing Tool Demo
Tool type: API Testing (Postman / RestAssured category)
Starts the local API server, then sends real HTTP requests and asserts
on status code + response body, exactly like a Postman test script does.
Run: python3 -m unittest tests/test_api.py -v
"""
import sys
import os
import json
import time
import unittest
import threading
import urllib.request
import urllib.error

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from api_server import HTTPServer, Handler

BASE_URL = "http://127.0.0.1:8899"


class TestAPI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server = HTTPServer(("127.0.0.1", 8899), Handler)
        cls.thread = threading.Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()
        time.sleep(0.3)

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()

    def test_health_status_code(self):
        resp = urllib.request.urlopen(f"{BASE_URL}/health")
        self.assertEqual(resp.getcode(), 200)

    def test_health_response_body(self):
        resp = urllib.request.urlopen(f"{BASE_URL}/health")
        body = json.loads(resp.read())
        self.assertEqual(body["status"], "ok")

    def test_add_endpoint(self):
        resp = urllib.request.urlopen(f"{BASE_URL}/add?a=5&b=7")
        body = json.loads(resp.read())
        self.assertEqual(body["result"], 12)

    def test_unknown_route_returns_404(self):
        with self.assertRaises(urllib.error.HTTPError) as ctx:
            urllib.request.urlopen(f"{BASE_URL}/does-not-exist")
        self.assertEqual(ctx.exception.code, 404)


if __name__ == "__main__":
    unittest.main()
