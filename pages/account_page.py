import allure

import data
from locators.account_page_locators import AccountPageLocators
from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.main_page import MainPage


class AccountPage(BasePage):
    URL = data.PageUrls.ACCOUNT_PAGE_URL

    @allure.step('Переход на страницу аккаунта')
    def go_to_account(self, email, password):
        LoginPage(self.driver).login(email, password)
        MainPage(self.driver).click_on_button_account()
        BasePage(self.driver).check_is_it_account_page()
        self._wait_visibility_of(AccountPageLocators.ACCOUNT_NAVIGATION)

    @allure.step('Клик на историю заказов')
    def click_on_order_history(self):
        self._click_on_element(AccountPageLocators.ORDER_HISTORY)

    @allure.step('Клик на кнопку выхода')
    def click_on_exit_button(self):
        self._click_on_element(AccountPageLocators.BUTTON_EXIT)

    @allure.step('Проверка на переход во вкладку истории заказов')
    def check_is_it_order_history(self):
        assert self._find_element(AccountPageLocators.ORDER_HISTORY_ACTIVE), 'Вкладка "История заказов" не активна'
