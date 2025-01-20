import allure

from locators.order_feed_page_locators import OrderFeedPageLocators

import data
from pages.base_page import BasePage


class OrderFeed(BasePage):
    random_order = None
    URL = data.PageUrls.ORDER_FEED_PAGE_URL

    def open(self):
        super().open()
        self._wait_visibility_of(OrderFeedPageLocators.ORDER_FEED)

    @allure.step("Клик по заказу")
    def click_on_order(self, ingredient):
        self._click_on_element(ingredient)

    @allure.step("Клик по случайному заказу")
    def click_on_random_order(self):
        self.random_order = self.get_random_component(OrderFeedPageLocators.ORDERS)
        self.click_on_order(self.random_order)

    @allure.step("Получить количество заказов за все время")
    def get_total_order_number(self):
        return self._find_element(OrderFeedPageLocators.TOTAL_ORDER_COUNTER).text

    @allure.step("Получить количество заказов за сегодня")
    def get_today_order_number(self):
        return self._find_element(OrderFeedPageLocators.TODAY_ORDER_COUNTER).text

    @allure.step("Проверка отображения деталей заказа")
    def check_is_order_details_opened(self):
        assert self._find_element(OrderFeedPageLocators.ORDER_DETAILS).is_displayed(), "Детали заказа не отображаются"

    @allure.step("Проверка наличия заказа в ленте")
    def check_is_order_in_feed(self, order_number):
        order_numbers = [number.text[2:] for number in self._find_elements(OrderFeedPageLocators.ORDER_NUMBERS)]

        assert str(order_number) in order_numbers, "Заказ в ленте отсутствует"

    @allure.step("Проверка наличия заказа в ленте")
    def check_is_order_cooking(self, order_number):
        self._wait_invisibility_of(OrderFeedPageLocators.EMPTY_COOKING_LIST)
        assert order_number in self._find_element(OrderFeedPageLocators.IN_COOKING_LIST).text, "Заказ не в работе"
