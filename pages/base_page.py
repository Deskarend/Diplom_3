from random import choice

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from seletools.actions import drag_and_drop


class BasePage:
    URL = None
    WAIT_TIME = 5

    OVERLAY = (By.XPATH, "//div[contains(@class, 'Modal_modal_overlay__x2ZCr')]/parent::div")

    BUTTON_ACCOUNT = (By.XPATH, ".//a[contains(@href, '/account')]")

    BUTTON_CONSTRUCTOR = (By.XPATH, ".//p[contains(text(),'Конструктор')]")
    BUTTON_ORDER_FEED = (By.XPATH, ".//p[contains(text(),'Лента Заказов')]")

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открыть страницу')
    def open(self):
        self.driver.get(self.URL)

    def _wait_visibility_of(self, element):
        WebDriverWait(self.driver, self.WAIT_TIME).until(EC.visibility_of_element_located(element))

    def _wait_invisibility_of(self, element):
        WebDriverWait(self.driver, self.WAIT_TIME).until(EC.invisibility_of_element_located(element))

    def _wait_clickable_of(self, element):
        self._wait_visibility_of(element)
        self._wait_invisibility_of(self.OVERLAY)
        WebDriverWait(self.driver, self.WAIT_TIME).until(EC.element_to_be_clickable(element))

    def _find_element(self, element):
        self._wait_visibility_of(element)
        return self.driver.find_element(*element)

    def _find_elements(self, elements):
        return self.driver.find_elements(*elements)

    def _scroll_to(self, element):
        web_element = self._find_element(element)
        self.driver.execute_script("arguments[0].scrollIntoView();", web_element)

    def _click_on_element(self, element):
        self._scroll_to(element)
        self._wait_clickable_of(element)
        self.driver.find_element(*element).click()

    def _check_element_has_text(self, element, text):
        element = self._find_element(*element)
        assert element.text == text, f"Ожидаемый текст {text}, фактический {element.text}"

    def _set_value_to_field(self, field_locator, value):
        self._find_element(field_locator).send_keys(value)
        actual_value = self._find_element(field_locator).get_attribute('value')
        assert value == actual_value, (f"Значение в поле не совпадает введенному. Ожидаемое значение {value}, "
                                       f"фактическое - {actual_value}")

    def _wait_changing_url(self):
        WebDriverWait(self.driver, self.WAIT_TIME).until(EC.url_changes(self.driver.current_url))

    def get_random_component(self, component):
        random_component = choice(self._find_elements(component))
        from pages.main_page import MainPage
        random_component = By.XPATH, (f".//a[contains(@href, '"
                                      f"{random_component.get_attribute('href')[len(MainPage.URL):]}')]")
        return random_component

    @allure.step('Клик на кнопку «Личный кабинет»')
    def click_on_button_account(self):
        self._click_on_element(self.BUTTON_ACCOUNT)

    @allure.step('Клик на кнопку «Конструктор»')
    def click_on_button_constructor(self):
        self._click_on_element(self.BUTTON_CONSTRUCTOR)

    @allure.step('Клик на кнопку «Лента Заказов»')
    def click_on_button_order_feed(self):
        self._click_on_element(self.BUTTON_ORDER_FEED)

    @allure.step('Перетащить элемент')
    def _drag_and_drop_element(self, element, target):
        drag_and_drop(self.driver, element, target)

    @allure.step('Проверка перехода на страницу восстановление пароля')
    def check_is_it_forgot_password_page(self):
        assert 'forgot-password' in self.driver.current_url, "Переход не на страницу восстановления пароля"

    @allure.step('Проверка перехода на главную страницу ')
    def check_is_it_main_page(self):
        from pages.main_page import MainPage
        assert self.driver.current_url == MainPage.URL, "Переход не на главную страницу"

    @allure.step('Проверка перехода на главную страницу после авторизации')
    def check_is_it_main_page_with_authorization(self):
        self._wait_changing_url()
        from pages.main_page import MainPage
        assert self._find_element(MainPage.BUTTON_ORDER).is_displayed(), "Пользователь не авторизован"

    @allure.step('Проверка перехода в "Личный кабинет"')
    def check_is_it_account_page(self):
        assert 'account' in self.driver.current_url, "Переход не в личный кабинет"

    @allure.step('Проверка перехода на страницу авторизации')
    def check_is_it_login_page(self):
        self._wait_changing_url()
        assert 'login' in self.driver.current_url, "Переход не на страницу авторизации"

    @allure.step('Проверка перехода на страницу ленты заказов')
    def check_is_it_order_feed_page(self):
        assert 'feed' in self.driver.current_url, "Переход не на страницу ленты заказов"

    @allure.step('Проверка увеличения счетчика')
    def check_is_counter_increased(self, new_counter, old_counter):
        assert new_counter > old_counter, "Счетчик не увеличился"
