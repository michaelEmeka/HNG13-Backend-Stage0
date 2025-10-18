import unittest
import requests
import datetime

class TestResponse(unittest.TestCase):
    def test_success_status(self):
        json_response = requests.get("http://127.0.0.1:8000/me")
        json_response_e = requests.get("http://127.0.0.1:8000/you")
        self.assertTrue(json_response.status_code, 200)
        self.assertTrue(json_response_e.status_code, 500)

    def test_timeout(self):
        json_response = requests.get("http://127.0.0.1:8000/me", timeout=5)
        self.assertIsInstance(json_response.json(), dict)
        self.assertTrue(json_response.status_code, 200)

    def test_required_header(self):
        json_response = requests.get("http://127.0.0.1:8000/me")
        self.assertEqual(json_response.headers.get("Content-Type"), "application/json")

    def test_response(self):
        json_response = requests.get("http://127.0.0.1:8000/me")
        json_response = json_response.json()
        self.assertEqual(json_response.get("status"), "success")
        self.assertDictEqual(json_response.get("user"),
                         {
                             "email": "mikelonu15@gmail.com",
                             "name": "Michael Onuekwusi",
                             "stack": "Django"
                             })
        self.assertIsInstance(json_response.get("fact"), str)
        self.assertTrue(len(json_response.get("fact")) > 0)

        self.assertIsInstance(
            datetime.time.fromisoformat(json_response.get("timestamp")),
            datetime.time
        )
    def test_invalid_method(self):
        json_response = requests.post("http://127.0.0.1:8000/me/")
        self.assertEqual(json_response.status_code, 500)

if __name__ == "__main__":
    unittest.main()
