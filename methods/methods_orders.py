import requests
from curl import Url

class OrdersMethods:

    @staticmethod
    def create_order(body):
        return requests.post(Url.CREATING_ORDERS, json=body)
    
    @staticmethod
    def cancel_order(track_id):
        payload = {"track": track_id}
        return requests.put(Url.CANCEL_ORDER, params=payload)
    
    @staticmethod
    def get_orders():
        return requests.get(Url.CREATING_ORDERS)