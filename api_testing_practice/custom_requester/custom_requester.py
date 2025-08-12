#custom_requester.py
import requests

class CustomRequester:
    def __init__(self, session, base_url):
        self.session = session
        self.base_url = base_url
        self.headers = {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }

    def send_request(self, method, endpoint, data=None, expected_status=200):
        url = f"{self.base_url}{endpoint}"
        response = self.session.request(
            method=method,
            url=url,
            json=data,
            headers=self.headers
        )

        assert response.status_code == expected_status, \
            f"Ожидали статус {expected_status}, но получили {response.status_code}"
        return response

