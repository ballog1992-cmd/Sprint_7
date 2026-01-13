import allure
import requests
from curl import Url

class OrdersMethods:

    
    @staticmethod
    @allure.step("Создать заказ")
    def create_order(body):
        return requests.post(Url.CREATING_ORDERS, json=body)
    
    
    @staticmethod
    @allure.step("Закрыть заказ с ID: {track_id}")
    def cancel_order(track_id):
        payload = {"track": track_id}
        return requests.put(Url.CANCEL_ORDER, params=payload)
    
    
    @staticmethod
    @allure.step("Получить список заказов")
    def get_orders():
        return requests.get(Url.CREATING_ORDERS)