import allure
import requests
from curl import Url


class CourierMethods:

    
    @staticmethod
    @allure.step("Создать курьера")
    def create_courier(body):
        return requests.post(Url.CREATING_COURIER_URL, json=body)
    
    
    @staticmethod
    @allure.step("Вход курьера в систему")
    def login_courier(login=None, password=None):
        
        payload = {}
        if login is not None:
            payload["login"] = login
        if password is not None:
            payload["password"] = password
        return requests.post(Url.COURIER_LOGIN_URL, json=payload)
    
    
    @staticmethod
    @allure.step("Удалить курьера")
    def delete_courier(login, password):

        login_courier = requests.post(
            Url.COURIER_LOGIN_URL, json={"login": login, "password": password}
        )

        if login_courier.status_code != 200:
            return login_courier

        courier_id = login_courier.json()["id"]
        delete_courier = requests.delete(f"{Url.CREATING_COURIER_URL}/{courier_id}")
        return delete_courier

    