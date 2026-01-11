import allure
import pytest
from methods.methods_orders import OrdersMethods
from request_data.data_orders import *
from helper import *

@allure.feature('Создание заказа')
class TestCreateOrder:

    @allure.title("Успешное создание заказа с разными вариантами цветов")
    @pytest.mark.parametrize("colors_list", [
        ["BLACK"], ["GREY"], 
        ["BLACK", "GREY"], 
        []
    ])
    def test_create_order_with_colors(self, colors_list, order_tracker):
        colors_lst = DataOrdersBody.ORDER_BODY_TEMPLATE.copy()
        colors_lst["color"] = colors_list

        response = OrdersMethods.create_order(colors_lst)

        track_id = response.json().get("track")
        order_tracker.append(track_id)

        assert response.status_code == DataOrdersCode.SUCCESSFUL_ORDER_CREATION_CODE
        assert "track" in response.json()
