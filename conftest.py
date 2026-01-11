import pytest
from helper import register_new_courier_and_return_login_password
from methods.courier_methods import CourierMethods
from methods.methods_orders import OrdersMethods

@pytest.fixture
def courier_body():

    body = register_new_courier_and_return_login_password()

    login = body["login"]
    password = body["password"]

    yield body

    CourierMethods.delete_courier(login, password)

@pytest.fixture
def order_tracker():

    track_id = []

    yield track_id

    OrdersMethods.cancel_order(track_id[0])