import allure
from selenium.webdriver.common.by import By


from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.main_page import MainPage


class AccountPage(BasePage):
    URl = 'https://stellarburgers.nomoreparties.site/account/profile'

    ACCOUNT_NAVIGATION = (By.XPATH, './/nav[contains(@class, "Account_nav")]')
    ORDER_HISTORY = (By.XPATH, ".//a[contains(@href, '/account/order-history')]")
    ORDER_HISTORY_ACTIVE = (By.XPATH, './/a[contains(@href,"/account/order-history") and contains(@class,'
                                      '"link_active")]')

    ORDER_HISTORY_LIST = (By.XPATH, './/ul[contains(@class, "OrderHistory_list")]')

    BUTTON_EXIT = (By.XPATH, ".//button[contains(text(), 'Выход')]")

    @allure.step('Переход на страницу аккаунта')
    def go_to_account(self, email, password):
        LoginPage(self.driver).login(email, password)
        MainPage(self.driver).click_on_button_account()
        BasePage(self.driver).check_is_it_account_page()
        self._wait_visibility_of(self.ACCOUNT_NAVIGATION)

    @allure.step('Клик на историю заказов')
    def click_on_order_history(self):
        self._click_on_element(self.ORDER_HISTORY)

    @allure.step('Проверка на переход во вкладку истории заказов')
    def check_is_it_order_history(self):
        assert self._find_element(self.ORDER_HISTORY_ACTIVE), 'Вкладка "История заказов" не активна'
        assert self._find_element(self.ORDER_HISTORY_LIST), 'Не отображается история заказов'

    @allure.step('Клик на кнопку выхода')
    def click_on_exit_button(self):
        self._click_on_element(self.BUTTON_EXIT)