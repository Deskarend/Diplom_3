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

    def _find_element(self, element):
        WebDriverWait(self.driver, self.WAIT_TIME).until(EC.visibility_of_element_located(element))
        return self.driver.find_element(*element)

    def _click_on_element(self, element):
        WebDriverWait(self.driver, self.WAIT_TIME).until(EC.element_to_be_clickable(element))
        self.driver.find_element(*element).click()

    def _check_element_has_text(self, element, text):
        element = self._find_element(*element)
        assert element.text == text, f"Ожидаемый текст {text}, фактический {element.text}"

    @allure.step('Проверка перехода на страницу восстановление пароля')
    def check_is_it_forgot_password_page(self):
        from pages.forgot_password_page import ForgotPassword
        assert EC.url_to_be(ForgotPassword.URL), "Переход не на страницу восстановления пароля"

    def _set_value_to_field(self, field_locator, value):
        self._find_element(field_locator).send_keys(value)
        actual_value = self._find_element(field_locator).get_attribute('value')
        assert value == actual_value, (f"Значение в поле не совпадает введенному. Ожидаемое значение {value}, "
                                       f"фактическое - {actual_value}")
