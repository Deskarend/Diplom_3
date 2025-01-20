import allure

import data
from locators.forgot_password_page_locators import ForgotPasswordPageLocators
from pages.base_page import BasePage


class ForgotPassword(BasePage):
    URL = data.PageUrls.FORGOT_PASSWORD_PAGE_URL

    @allure.step('Нажать на кнопку "Восстановить"')
    def click_on_button_reset(self):
        self._click_on_element(ForgotPasswordPageLocators.BUTTON_RESET)

    @allure.step('Ввести email')
    def set_email(self, email):
        self._set_value_to_field(ForgotPasswordPageLocators.FIELD_EMAIL, email)

    @allure.step('Проверка отображения полей "Пароль" и "Введите код из письма"')
    def check_is_it_reset_password_form(self):
        assert self._find_element(ForgotPasswordPageLocators.FIELD_NEW_PASSWORD).is_displayed(), \
            'Поле "Пароль не отображается"'
        assert self._find_element(ForgotPasswordPageLocators.FIELD_EMAIL_CODE).is_displayed(), \
            'Поле "Введите код из письма"'

    @allure.step('Перейти к форме восстановления пароля')
    def go_to_form_reset_password(self, email):
        self.open()
        self.set_email(email)
        self.click_on_button_reset()
        self.check_is_it_reset_password_form()

    @allure.step('Нажать на кнопку показать/скрыть пароль')
    def click_on_button_show_or_hide_password(self):
        self._click_on_element(ForgotPasswordPageLocators.BUTTON_SHOW_OR_HIDE_PASSWORD)

    @allure.step('Проверка поле "Пароль" в фокусе')
    def check_is_field_password_focused(self):
        assert self._find_element(ForgotPasswordPageLocators.FIELD_NEW_PASSWORD_IS_FOCUSED).is_displayed(), \
            'Поле "Пароль" не в фокусе'
