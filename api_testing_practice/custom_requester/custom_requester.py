#custom_requester.py
import requests

class CustomRequester:
    def __init__(self, session, base_url):
        self.session: requests.Session = session
        self.base_url = base_url
        self.session.headers.update({
            "Content-Type": "application/json",
            "Accept": "application/json"
        })

    def send_request(self, method, endpoint, data=None, expected_status=200):
        url = f"{self.base_url}{endpoint}"
        response = self.session.request(
            method=method,
            url=url,
            json=data
        )

        assert response.status_code == expected_status, \
            f"Ожидали статус {expected_status}, но получили {response.status_code}"
        return response

    def send_request_from_id(self, method, endpoint, movie_id, data=None, expected_status=200):
        url = f"{self.base_url}{endpoint}/{movie_id}"
        response = self.session.request(
            method=method,
            url=url,
            json=data
        )

        assert response.status_code == expected_status, \
            f"Ожидали статус {expected_status}, но получили {response.status_code}"
        return response

