#custom_requester.py
import requests
import logging


class CustomRequester:
    def __init__(self, session, base_url):
        self.session: requests.Session = session
        self.base_url = base_url
        self.session.headers.update({
            "Content-Type": "application/json",
            "Accept": "application/json"
        })
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)

    def send_request(self, method, endpoint, params=None, data=None, expected_status=200):
        response = self.session.request(
            method=method,
            url=f"{self.base_url}{endpoint}",
            params=params,
            json=data

        )

        assert response.status_code == expected_status, \
            f"Ожидали статус {expected_status}, но получили {response.status_code}"
        return response

