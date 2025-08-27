#custom_requester.py
import pytest
import requests


class CustomRequester:
    def __init__(self, session, base_url):
        self.session: requests.Session = session
        self.base_url = base_url
        self.session.headers.update({
            "Content-Type": "application/json",
            "Accept": "application/json"
        })


    def send_request(self, method, endpoint, params=None, data=None, expected_status=200):

        print(f"Отправляю: {method} запрос на: {endpoint}")

        if data:
            print(f"Отправляю data: {data}")
        if params:
            print(f"Отправляю params: {params}")

        response = self.session.request(
            method=method,
            url=f"{self.base_url}{endpoint}",
            params=params,
            json=data
        )
        print(f"Получил ответ:{response.status_code}")
        print(f"Получил ответ:{response.json()}")

        if response.status_code != expected_status:
            print(f"Текст ошибки: {response.text}")
            pytest.fail(f"Ожидали статус {expected_status}, но получили {response.status_code}")
        else:
            print("Успех!")

        return response


