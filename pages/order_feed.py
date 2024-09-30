import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class OrderFeed(BasePage):
    random_order = None
    URL = "https://stellarburgers.nomoreparties.site/feed"

    ORDER_FEED = (By.XPATH, ".//div[contains(@class, 'orderFeed')]")

    ORDERS = (By.XPATH, ".//a[contains(@href, '/feed/')]")
    ORDER_DETAILS = (By.XPATH, ".//section[contains(@class, 'opened')]//div[contains(@class, 'orderBox')]")

    ORDER_NUMBERS = (By.XPATH, ".//div[contains(@class, 'textBox')]//p[contains(@class, 'digits')]")

    TOTAL_ORDER_COUNTER = (By.XPATH, ".//p[contains(text(), 'за все время')]/following-sibling::p")
    TODAY_ORDER_COUNTER = (By.XPATH, ".//p[contains(text(), 'за сегодня')]/following-sibling::p")

    IN_COOKING_LIST = (By.XPATH, ".//ul[contains(@class, 'ListReady')]")
    EMPTY_COOKING_LIST = (By.XPATH, ".//li[contains(text(), 'заказы готовы')]")

    def open(self):
        super().open()
        self._wait_visibility_of(self.ORDER_FEED)

    @allure.step("Клик по заказу")
    def click_on_order(self, ingredient):
        self._click_on_element(ingredient)

    @allure.step("Клик по случайному заказу")
    def click_on_random_order(self):
        self.random_order = self.get_random_component(self.ORDERS)
        self.click_on_order(self.random_order)

    @allure.step("Получить количество заказов за все время")
    def get_total_order_number(self):
        return self._find_element(self.TOTAL_ORDER_COUNTER).text

    @allure.step("Получить количество заказов за сегодня")
    def get_today_order_number(self):
        return self._find_element(self.TODAY_ORDER_COUNTER).text

    @allure.step("Проверка отображения деталей заказа")
    def check_is_order_details_opened(self):
        assert self._find_element(self.ORDER_DETAILS).is_displayed(), "Детали заказа не отображаются"

    @allure.step("Проверка наличия заказа в ленте")
    def check_is_order_in_feed(self, order_number):
        order_numbers = [number.text for number in self._find_elements(self.ORDER_NUMBERS)]
        assert order_number in order_numbers, "Заказ в ленте отсутствует"

    @allure.step("Проверка наличия заказа в ленте")
    def check_is_order_cooking(self, order_number):
        self._wait_invisibility_of(self.EMPTY_COOKING_LIST)
        assert order_number in self._find_element(self.IN_COOKING_LIST).text, "Заказ не в работе"
