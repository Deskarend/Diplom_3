import allure

from selenium.webdriver.support import expected_conditions as EC

import data
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    random_ingredient = None

    random_bun = None
    random_sauce = None
    random_filling = None

    number_random_order = None

    URL = data.PageUrls.MAIN_PAGE_URL

    @allure.step("Клик по ингредиенту")
    def click_on_ingredient(self, ingredient):
        self._click_on_element(ingredient)

    @allure.step("Клик по случайному ингредиенту")
    def click_on_random_ingredient(self):
        self.random_ingredient = self.get_random_component(MainPageLocators.INGREDIENTS)
        self.click_on_ingredient(self.random_ingredient)

    @allure.step("Добавить случайный ингредиент в заказ")
    def add_random_ingredient_on_order(self):
        self.random_ingredient = self.get_random_component(MainPageLocators.INGREDIENTS)
        random_ingredient = self._find_element(self.random_ingredient)
        basket = self._find_element(MainPageLocators.BASKET)
        self._drag_and_drop_element(random_ingredient, basket)

    @allure.step("Добавить случайный бургер в заказ")
    def add_random_burger_on_order(self):
        self.random_bun = self.get_random_component(MainPageLocators.BUNS)
        random_bun = self._find_element(self.random_bun)

        self.random_sauce = self.get_random_component(MainPageLocators.SAUCES)
        random_sauce = self._find_element(self.random_sauce)

        self.random_filling = self.get_random_component(MainPageLocators.FILLINGS)
        random_filling = self._find_element(self.random_filling)

        basket = self._find_element(MainPageLocators.BASKET)

        self._drag_and_drop_element(random_bun, basket)
        self._drag_and_drop_element(random_sauce, basket)
        self._drag_and_drop_element(random_filling, basket)

    @allure.step("Оформить случайный заказ")
    def place_random_order(self):
        self.add_random_burger_on_order()
        self.click_on_button_place_order()
        self._wait_invisibility_of(MainPageLocators.NOT_UPLOADED_ORDER_NUMBER)
        self.number_random_order = self._find_element(MainPageLocators.ORDER_NUMBER).text

    @allure.step("Получение номера оформленного заказа")
    def get_order_number(self):
        return self.number_random_order

    @allure.step("Клик по крестику в деталях ингредиента")
    def close_ingredient_detail(self):
        self._click_on_element(MainPageLocators.BUTTON_CLOSE_INGREDIENTS_DETAILS)

    @allure.step("Клик по кнопке 'Оформить заказ'")
    def click_on_button_place_order(self):
        self._click_on_element(MainPageLocators.BUTTON_ORDER)

    @allure.step("Проверка отображения деталей ингредиента")
    def check_is_ingredient_details_opened(self):
        assert self._find_element(
            MainPageLocators.INGREDIENT_DETAILS).is_displayed(), "Детали ингредиентов не отображаются"

    @allure.step("Проверка отсутствия деталей ингредиента")
    def check_is_ingredient_details_closed(self):
        assert EC.invisibility_of_element(MainPageLocators.INGREDIENT_DETAILS), "Детали ингредиентов  отображаются"

    @allure.step("Проверка увеличения счетчика ингредиента")
    def check_is_ingredient_counter_increased(self):
        assert int(self._find_element(self.random_ingredient).text[0]) > 0, "Счетчик не увеличился"

    @allure.step("Проверка подтверждения заказа")
    def check_is_order_confirmed(self):
        assert self._find_element(
            MainPageLocators.ORDER_CONFIRMATION).is_displayed(), "Подтверждение заказа отсутствует"
