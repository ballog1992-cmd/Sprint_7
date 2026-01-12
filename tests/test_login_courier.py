import allure
import pytest
from methods.courier_methods import CourierMethods
from request_data.data_courier import DataRequestCode, DataRequestBody
from request_data.data_orders import *
from curl import Url

@allure.feature('Логин курьера')
class TestLoginCourier:

    @allure.title("Успешная авторизация курьера")
    def test_login_courier_valid_credentials_success(self, registered_courier):
        response = CourierMethods.login_courier(registered_courier["login"], registered_courier["password"])
        assert response.status_code == DataRequestCode.OK
        assert "id" in response.json()

    @allure.title("Cистема вернёт ошибку, если авторизоваться под несуществующим пользователем")
    def test_login_courier_non_existent_user_not_found_error(self):
        data = non_existent_courier_body()
        response = CourierMethods.login_courier(data["login"], data["password"])
        
        assert response.status_code == DataRequestCode.NOT_FOUND
        assert response.json()["message"] == DataRequestBody.LOGIN_NOT_FOUND

    @allure.title("Cистема вернёт ошибку, если неправильно указать пароль")
    def test_login_courier_incorrect_password_not_found_error(self, registered_courier):
        data = non_existent_courier_body()
        response = CourierMethods.login_courier(registered_courier["login"], data["password"])
        
        assert response.status_code == DataRequestCode.NOT_FOUND
        assert response.json()["message"] == DataRequestBody.LOGIN_NOT_FOUND

    @allure.title("Cистема вернёт ошибку, если неправильно указать логин")
    def test_login_courier_incorrect_login_not_found_error(self, registered_courier):
        data = non_existent_courier_body()
        response = CourierMethods.login_courier(data["login"], registered_courier["password"])
        
        assert response.status_code == DataRequestCode.NOT_FOUND
        assert response.json()["message"] == DataRequestBody.LOGIN_NOT_FOUND

    @allure.title("Ошибка авторизации при отсутствии обязательного поля")
    @allure.description("Баг: Сервер возвращает 504 вместо 400 Bad Request при отсутствии поля password")
    @pytest.mark.xfail(reason="Баг API: Сервер не верно возвращает код ошибки при оставлении поля password пустым")
    @pytest.mark.parametrize("field", ["login", "password"])
    def test_login_courier_missing_required_field_bad_request(self, registered_courier, field):
        test_data = registered_courier.copy()

        test_data.pop("firstName", None)
        test_data.pop(field)

        response = CourierMethods.login_courier(**test_data)
        assert response.status_code == DataRequestCode.BAD_REQUEST
        assert response.json()["message"] == DataRequestBody.LOGIN_COURIER_DATA
