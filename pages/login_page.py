import allure

import data
from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):
    URL = data.PageUrls.LOGIN_PAGE_URL

    @allure.step('Клик на кнопку «Восстановить пароль»')
    def click_on_button_forgot_password(self):
        self._click_on_element(LoginPageLocators.BUTTON_FORGOT_PASSWORD)

    @allure.step('Заполнить поле "Email"')
    def set_email(self, email):
        self._set_value_to_field(LoginPageLocators.INPUT_EMAIL, email)

    @allure.step('Заполнить поле "Пароль"')
    def set_password(self, password):
        self._set_value_to_field(LoginPageLocators.INPUT_PASSWORD, password)

    @allure.step('Клик на кнопку «Войти»')
    def click_on_button_login(self):
        self._click_on_element(LoginPageLocators.BUTTON_LOGIN)

    @allure.step('Логик в аккаунт')
    def login(self, email, password):
        self.open()
        self.set_email(email)
        self.set_password(password)
        self.click_on_button_login()
        self.check_is_it_main_page_with_authorization()
