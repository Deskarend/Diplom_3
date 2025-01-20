import allure
import requests

from api_modules.base_endpoint import BaseEndpoint


class DeleteUser(BaseEndpoint):
    DELETE_USER_ENDPOINT = 'api/auth/user'

    @allure.step('Удаление пользователя')
    def delete_user(self, token):
        self.response = requests.delete(self.BASE_URL + self.DELETE_USER_ENDPOINT, headers={"Authorization": token})
