import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    URL = None
    WAIT_TIME = 5

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открыть страницу')
    def open(self):
        self.driver.get(self.URL)

    def _wait_visibility_of(self, element):
        WebDriverWait(self.driver, self.WAIT_TIME).until(EC.visibility_of_element_located(element))

    def _wait_clickable_of(self, element):
        WebDriverWait(self.driver, self.WAIT_TIME).until(EC.element_to_be_clickable(element))

    def _find_element(self, element):
        self._wait_visibility_of(element)
        return self.driver.find_element(*element)

    def _click_on_element(self, element):
        el = self._find_element(element)
        self._wait_clickable_of(element)
        el.click()

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

    @allure.step('Проверка перехода на страницу восстановление пароля')
    def check_is_it_forgot_password_page(self):
        self._wait_changing_url()
        assert 'forgot-password' in self.driver.current_url, "Переход не на страницу восстановления пароля"

    @allure.step('Проверка перехода на главную страницу после авторизации')
    def check_is_it_main_page_with_authorization(self):
        self._wait_changing_url()
        from pages.main_page import MainPage
        assert self._find_element(MainPage.BUTTON_ORDER).is_displayed(), "Пользователь не авторизован"

    @allure.step('Проверка перехода в "Личный кабинет"')
    def check_is_it_account_page(self):
        self._wait_changing_url()
        assert 'account' in self.driver.current_url, "Переход не в личный кабинет"

    @allure.step('Проверка перехода на страницу авторизации')
    def check_is_it_login_page(self):
        self._wait_changing_url()
        assert 'login' in self.driver.current_url, "Переход не на страницу авторизации"
