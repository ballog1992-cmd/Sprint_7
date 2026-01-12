import allure
import pytest
from methods.courier_methods import CourierMethods
from request_data.data_courier import DataRequestCode, DataRequestBody
from helper import *

@allure.feature('Создание курьера')
class TestCreateCourier:

    @allure.title("Успешное создание курьера")
    def test_create_courier_valid_data_success(self, courier_data):
        response = CourierMethods.create_courier(courier_data)
        assert response.status_code == DataRequestCode.CREATED
        assert response.json() == DataRequestBody.OK_TRUE
    
    @allure.title("Нельзя создать двух одинаковых курьеров")
    @allure.description("Баг: Сервер возвращает 'Этот логин уже используется. Попробуйте другой.' вместо 'Этот логин уже используется' при создании дубликата")
    @pytest.mark.xfail(reason="Баг API: Сервер не верно возвращает тело сообщения об уже использованном логине")
    def test_create_courier_duplicate_login_conflict_error(self, registered_courier):
        response = CourierMethods.create_courier(registered_courier)
        assert response.status_code == DataRequestCode.CONFLICT
        assert response.json()["message"] == DataRequestBody.CREATE_DUPLICATE_LOGIN

    @allure.title("Ошибка при создании курьера без обязательных полей")
    @pytest.mark.parametrize("field", ["login", "password"])
    def test_create_courier_missing_required_field_bad_request(self, courier_data, field):
        courier_data.pop(field)
        response = CourierMethods.create_courier(courier_data)
        assert response.status_code == DataRequestCode.BAD_REQUEST
        assert response.json()["message"] == DataRequestBody.CREATE_COURIER_DATA
