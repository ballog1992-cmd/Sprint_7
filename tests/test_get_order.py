import allure
from methods.methods_orders import OrdersMethods
from request_data.data_orders import *
from helper import *

@allure.feature('Список заказов')
class TestOrderList:

    @allure.title("Проверка получения списка заказов")
    def test_get_orders_list_returns_list(self):

        response = OrdersMethods.get_orders()

        assert response.status_code == DataOrdersCode.SUCCESSFUL_LIST_ORDERS
        assert "orders" in response.json()
        assert isinstance(response.json()["orders"], list)