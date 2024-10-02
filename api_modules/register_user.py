import allure
import requests

from api_modules.base_endpoint import BaseEndpoint


class RegisterUser(BaseEndpoint):
    REGISTER_ENDPOINT = 'api/auth/register'

    @allure.step("Регистрация пользователя")
    def create_user(self, payload):
        self.response = requests.post(self.BASE_URL + self.REGISTER_ENDPOINT, json=payload)
        self.response_json = self.response.json()
        self.access_token = self.response_json.get('accessToken')

    @allure.step("Получение токена для авторизации")
    def get_access_token(self):
        return self.access_token
