import allure
import pytest
from methods.courier_methods import CourierMethods
from request_data.data_courier import DataRequestCode, DataRequestBody
from helper import *

@allure.feature('Создание курьера')
class TestCreateCourier:

    @allure.title("Успешное создание курьера")
    def test_success_create_courier_valid_data(self, courier_body):
        response = CourierMethods.create_courier(courier_body)
        assert response.status_code == DataRequestCode.CREATED
        assert response.json() == DataRequestBody.OK_TRUE
    
    @allure.title("Нельзя создать двух одинаковых курьеров")
    @allure.description("Баг: Сервер возвращает 'Этот логин уже используется. Попробуйте другой.' вместо 'Этот логин уже используется' при создании дубликата")
    @pytest.mark.xfail(reason="Баг API: Сервер не верно возвращает тело сообщения об уже использованном логине")
    def test_system_return_an_error_enter_create_duplicate_courier(self, courier_body):
        CourierMethods.create_courier(courier_body)
        response = CourierMethods.create_courier(courier_body)
        assert response.status_code == DataRequestCode.CONFLICT
        assert response.json()["message"] == DataRequestBody.CREATE_DUPLICATE_LOGIN

    @allure.title("Ошибка при создании курьера без обязательных полей")
    @pytest.mark.parametrize("field", ["login", "password"])
    def test_system_return_an_error_entercreate_without_no_required_field(self, courier_body, field):
        courier_body.pop(field)
        response = CourierMethods.create_courier(courier_body)
        assert response.status_code == DataRequestCode.BAD_REQUEST
        assert response.json()["message"] == DataRequestBody.CREATE_COURIER_DATA
    
    @allure.title("Ошибка при создании курьера с уже существующим логином")
    @allure.description("Баг: Сервер возвращает 'Этот логин уже используется. Попробуйте другой.' вместо 'Этот логин уже используется' при создании курьера с уже существующим логином")
    @pytest.mark.xfail(reason="Баг API: Сервер не верно возвращает тело сообщения об уже использованном логине")
    def test_system_return_an_error_creating_courier_an_existing_login(self, courier_body):
        CourierMethods.create_courier(courier_body)
        data_two_courier = register_new_courier_and_return_login_password()
        data_two_courier["login"] = courier_body["login"]
        response = CourierMethods.create_courier(data_two_courier)
        assert response.status_code == DataRequestCode.CONFLICT
        assert response.json()["message"] == DataRequestBody.CREATE_DUPLICATE_LOGIN