import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ForgotPassword(BasePage):
    URL = 'https://stellarburgers.nomoreparties.site/forgot-password'

    BUTTON_RESET = (By.XPATH, './/button[contains(text(),"Восстановить")]')
    FIELD_EMAIL = (By.XPATH, './/label[contains(text(),"Email")]/following-sibling::input')

    FIELD_NEW_PASSWORD = (By.XPATH, './/input[contains(@name,"пароль")]')
    FIELD_NEW_PASSWORD_IS_FOCUSED = (By.XPATH, './/div[contains(@class, "status_active")]')
    FIELD_EMAIL_CODE = (By.XPATH, './/label[contains(text(),"код")]/following-sibling::input')

    BUTTON_SHOW_OR_HIDE_PASSWORD = (By.XPATH, './/div[contains(@class, "icon-action")]')

    @allure.step('Нажать на кнопку "Восстановить"')
    def click_on_button_reset(self):
        self._click_on_element(self.BUTTON_RESET)

    @allure.step('Ввести email')
    def set_email(self, email):
        self._set_value_to_field(self.FIELD_EMAIL, email)

    @allure.step('Проверка отображения полей "Пароль" и "Введите код из письма"')
    def check_are_fields_new_password_and_email_code_displayed(self):
        assert self._find_element(self.FIELD_NEW_PASSWORD).is_displayed(), 'Поле "Пароль не отображается"'
        assert self._find_element(self.FIELD_EMAIL_CODE).is_displayed(), 'Поле "Введите код из письма"'

    @allure.step('Перейти к форме восстановления пароля')
    def go_to_form_reset_password(self, email):
        self.open()
        self.set_email(email)
        self.click_on_button_reset()
        self.check_are_fields_new_password_and_email_code_displayed()

    @allure.step('Нажать на кнопку показать/скрыть пароль')
    def click_on_button_show_or_hide_password(self):
        self._click_on_element(self.BUTTON_SHOW_OR_HIDE_PASSWORD)

    @allure.step('Проверка поле "Пароль" в фокусе')
    def check_is_field_password_focused(self):
        assert self._find_element(self.FIELD_NEW_PASSWORD_IS_FOCUSED).is_displayed(), 'Поле "Пароль" не в фокусе'
