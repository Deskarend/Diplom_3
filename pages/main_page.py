from random import choice

import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class MainPage(BasePage):
    random_ingredient = None

    random_bun = None
    random_sauce = None
    random_filling = None

    URL = "https://stellarburgers.nomoreparties.site/"

    BUTTON_ACCOUNT = (By.XPATH, ".//a[contains(@href, '/account')]")

    BUTTON_ORDER = (By.XPATH, ".//button[contains(text(),'заказ')]")

    BUTTON_CONSTRUCTOR = (By.XPATH, ".//p[contains(text(),'Конструктор')]")

    INGREDIENTS = (By.XPATH, ".//a[contains(@href, '/ingredient/')]")
    INGREDIENT_DETAILS = (By.XPATH, ".//section[contains(@class, 'opened')]//h2[contains(text(), 'Детали')]")
    BUTTON_CLOSE_INGREDIENTS_DETAILS = (By.XPATH,
                                        ".//section[contains(@class, 'opened')]//button[contains(@class, 'close')]")

    BASKET = (By.XPATH, ".//ul[contains(@class, 'basket')]")

    BUNS = (By.XPATH, ".//ul[1]/a[contains(@href, 'ingredient')]")
    SAUCES = (By.XPATH, ".//ul[2]/a[contains(@href, 'ingredient')]")
    FILLINGS = (By.XPATH, ".//ul[3]/a[contains(@href, 'ingredient')]")

    ORDER_CONFIRMATION = (By.XPATH,
                          ".//section[contains(@class, 'opened')]//p[contains(text(), 'заказ начали готовить')]")

    def get_random_component(self, component):
        random_component = choice(self._find_elements(component))
        random_component = By.XPATH, (f".//a[contains(@href, '"
                                      f"{random_component.get_attribute('href')[len(MainPage.URL):]}')]")
        return random_component

    @allure.step("Клик по ингредиенту")
    def click_on_ingredient(self, ingredient):
        self._click_on_element(ingredient)

    @allure.step("Клик по случайному ингредиенту")
    def click_on_random_ingredient(self):
        self.random_ingredient = self.get_random_component(self.INGREDIENTS)
        self.click_on_ingredient(self.random_ingredient)

    @allure.step("Добавить случайный ингредиент в заказ")
    def add_random_ingredient_on_order(self):
        self.random_ingredient = self.get_random_component(self.INGREDIENTS)
        random_ingredient = self._find_element(self.random_ingredient)
        basket = self._find_element(self.BASKET)
        action = ActionChains(self.driver)
        action.drag_and_drop(random_ingredient, basket).perform()

    @allure.step("Добавить случайный бургер в заказ")
    def add_random_burger_on_order(self):
        self.random_bun = self.get_random_component(self.BUNS)
        random_bun = self._find_element(self.random_bun)

        self.random_sauce = self.get_random_component(self.SAUCES)
        random_sauce = self._find_element(self.random_sauce)

        self.random_filling = self.get_random_component(self.FILLINGS)
        random_filling = self._find_element(self.random_filling)

        basket = self._find_element(self.BASKET)

        action = ActionChains(self.driver)

        action.drag_and_drop(random_bun, basket).perform()
        action.drag_and_drop(random_sauce, basket).perform()
        action.drag_and_drop(random_filling, basket).perform()

    @allure.step("Клик по крестику в деталях ингредиента")
    def close_ingredient_detail(self):
        self._click_on_element(self.BUTTON_CLOSE_INGREDIENTS_DETAILS)

    @allure.step("Клик по кнопке 'Оформить заказ'")
    def click_on_button_place_order(self):
        self._click_on_element(self.BUTTON_ORDER)

    @allure.step("Проверка отображения деталей ингредиента")
    def check_is_ingredient_details_opened(self):
        assert self._find_element(self.INGREDIENT_DETAILS).is_displayed(), "Детали ингредиентов не отображаются"

    @allure.step("Проверка отсутствия деталей ингредиента")
    def check_is_ingredient_details_closed(self):
        assert EC.invisibility_of_element(self.INGREDIENT_DETAILS), "Детали ингредиентов  отображаются"

    @allure.step("Проверка увеличения счетчика ингредиента")
    def check_is_ingredient_counter_increased(self):
        assert int(self._find_element(self.random_ingredient).text[0]) > 0, "Счетчик не увеличился"

    @allure.step("Проверка подтверждения заказа")
    def check_is_order_confirmed(self):
        assert self._find_element(self.ORDER_CONFIRMATION).is_displayed(), "Подтверждение заказа отсутствует"
