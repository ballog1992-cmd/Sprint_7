import pytest
from helper import register_new_courier_and_return_login_password
from methods.courier_methods import CourierMethods
from methods.methods_orders import OrdersMethods
from request_data.data_orders import DataOrdersBody
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
def order_tracker(request):

    order_body = DataOrdersBody.ORDER_BODY_TEMPLATE.copy()
    order_body.update(request.param)

    response = OrdersMethods.create_order(order_body)
    track_id = response.json().get("track")
    

    yield response

    if track_id:

        OrdersMethods.cancel_order(track_id)
    else:
        print (" Заказ не найден, список пуст")