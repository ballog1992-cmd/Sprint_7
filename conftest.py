import pytest
from helper import register_new_courier_and_return_login_password
from methods.courier_methods import CourierMethods
from methods.methods_orders import OrdersMethods

@pytest.fixture
def courier_data():
    return register_new_courier_and_return_login_password()

@pytest.fixture
def registered_courier(courier_data):

    courier_body = courier_data.copy()
    CourierMethods.create_courier(courier_body)

    yield courier_data

    CourierMethods.delete_courier(courier_data["login"], courier_data["password"])

@pytest.fixture
def order_tracker():

    track_id = []

    yield track_id

    for i in track_id:

        OrdersMethods.cancel_order(i)
    else:
         print (" Заказ не найден, список пуст")