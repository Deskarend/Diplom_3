import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):
    URL = 'https://stellarburgers.nomoreparties.site/login'

    BUTTON_FORGOT_PASSWORD = (By.XPATH, ".//a[contains(@href,'/forgot-password')]")

    @allure.step('Клик на кнопку «Восстановить пароль»')
    def click_on_button_forgot_password(self):
        self._click_on_element(self.BUTTON_FORGOT_PASSWORD)
