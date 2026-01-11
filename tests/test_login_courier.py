import allure
import pytest
from methods.courier_methods import CourierMethods
from request_data.data_courier import DataRequestCode, DataRequestBody
from helper import *
from curl import Url

@allure.feature('Логин курьера')
class TestLoginCourier:

    @allure.title("Успешная авторизация курьера")
    def test_success_login_valid_data(self, courier_body):
        CourierMethods.create_courier(courier_body)
        response = CourierMethods.login_courier(courier_body["login"], courier_body["password"])
        assert response.status_code == DataRequestCode.OK
        assert "id" in response.json()

    @allure.title("Cистема вернёт ошибку, если авторизоваться под несуществующим пользователем")
    def test_system_return_an_error_login_non_existent_courier(self):
        data = non_existent_courier_body()
        response = CourierMethods.login_courier(data["login"], data["password"])
        
        assert response.status_code == DataRequestCode.NOT_FOUND
        assert response.json()["message"] == DataRequestBody.LOGIN_NOT_FOUND

    @allure.title("Cистема вернёт ошибку, если неправильно указать пароль")
    def test_system_return_an_error_enter_an_incorrect_password(self, courier_body):
        CourierMethods.create_courier(courier_body)
        data = non_existent_courier_body()
        response = CourierMethods.login_courier(courier_body["login"], data["password"])
        
        assert response.status_code == DataRequestCode.NOT_FOUND
        assert response.json()["message"] == DataRequestBody.LOGIN_NOT_FOUND

    @allure.title("Cистема вернёт ошибку, если неправильно указать логин")
    def test_system_return_an_error_enter_an_incorrect_login(self, courier_body):
        CourierMethods.create_courier(courier_body)
        data = non_existent_courier_body()
        response = CourierMethods.login_courier(courier_body["password"], data["login"])
        
        assert response.status_code == DataRequestCode.NOT_FOUND
        assert response.json()["message"] == DataRequestBody.LOGIN_NOT_FOUND

    @allure.title("Ошибка авторизации при отсутствии обязательного поля")
    @allure.description("Баг: Сервер возвращает 504 вместо 400 Bad Request при отсутствии поля password")
    @pytest.mark.xfail(reason="Баг API: Сервер не верно возвращает код ошибки при оставлении поля password пустым")
    @pytest.mark.parametrize("field", ["login", "password"])
    def test_system_return_an_error_required_field_missing(self, courier_body, field):
        CourierMethods.create_courier(courier_body)
        courier_body.pop(field)
        response = requests.post(Url.COURIER_LOGIN_URL, json=courier_body)
        assert response.status_code == DataRequestCode.BAD_REQUEST
        assert response.json()["message"] == DataRequestBody.LOGIN_COURIER_DATA
