import requests
from curl import Url


class CourierMethods:
    @staticmethod
    def create_courier(body):
        return requests.post(Url.CREATING_COURIER_URL, json=body)

    @staticmethod
    def login_courier(login, password):
        payload = {"login": login, "password": password}
        return requests.post(Url.COURIER_LOGIN_URL, json=payload)

    @staticmethod
    def delete_courier(login, password):

        login_courier = requests.post(
            Url.COURIER_LOGIN_URL, json={"login": login, "password": password}
        )

        if login_courier.status_code != 200:
            return login_courier

        courier_id = login_courier.json()["id"]
        delete_courier = requests.delete(f"{Url.CREATING_COURIER_URL}/{courier_id}")
        return delete_courier

    