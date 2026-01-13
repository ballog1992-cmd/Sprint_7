import allure
import pytest
from methods.methods_orders import OrdersMethods
from request_data.data_orders import *
from helper import *

@allure.feature('Создание заказа')
class TestCreateOrder:

    @allure.title("Успешное создание заказа с разными вариантами цветов")
    @pytest.mark.parametrize("order_tracker", [
        {"color": ["BLACK"]}, {"color": ["GREY"]},
        {"color": ["BLACK", "GREY"]}, 
        {"color": []}], indirect=True)
    def test_create_order_various_colors_track_id_received(self, order_tracker):
        
        assert order_tracker.status_code == DataOrdersCode.SUCCESSFUL_ORDER_CREATION_CODE
        assert "track" in order_tracker.json()
        
