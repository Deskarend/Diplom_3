import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):
    URL = 'https://stellarburgers.nomoreparties.site/login'

    BUTTON_FORGOT_PASSWORD = (By.XPATH, ".//a[contains(@href,'/forgot-password')]")

    INPUT_EMAIL = (By.XPATH, ".//input[@name='name']")
    INPUT_PASSWORD = (By.XPATH, ".//input[@name='Пароль']")
    BUTTON_LOGIN = (By.XPATH, ".//button[contains(text(), 'Войти')]")

    @allure.step('Клик на кнопку «Восстановить пароль»')
    def click_on_button_forgot_password(self):
        self._click_on_element(self.BUTTON_FORGOT_PASSWORD)

    @allure.step('Заполнить поле "Email"')
    def set_email(self, email):
        self._set_value_to_field(self.INPUT_EMAIL, email)

    @allure.step('Заполнить поле "Пароль"')
    def set_password(self, password):
        self._set_value_to_field(self.INPUT_PASSWORD, password)

    @allure.step('Клик на кнопку «Войти»')
    def click_on_button_login(self):
        self._click_on_element(self.BUTTON_LOGIN)

    @allure.step('Логик в аккаунт')
    def login(self, email, password):
        self.open()
        self.set_email(email)
        self.set_password(password)
        self.click_on_button_login()
        self.check_is_it_main_page_with_authorization()
