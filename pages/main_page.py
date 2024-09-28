import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class MainPage(BasePage):
    URL = "https://stellarburgers.nomoreparties.site"

    BUTTON_ACCOUNT = (By.XPATH, ".//a[contains(@href, '/account')]")

    BUTTON_ORDER = (By.XPATH, ".//button[contains(text(),'заказ')]")

    @allure.step('Клик на кнопку «Личный кабинет»')
    def click_on_button_account(self):
        self._click_on_element(self.BUTTON_ACCOUNT)