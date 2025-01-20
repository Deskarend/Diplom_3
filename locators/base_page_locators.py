from selenium.webdriver.common.by import By

import data


class BasePageLocators:
    OVERLAY = (By.XPATH, "//div[contains(@class, 'Modal_modal_overlay__x2ZCr')]/parent::div")

    BUTTON_ACCOUNT = (By.XPATH, ".//a[contains(@href, '/account')]")

    BUTTON_CONSTRUCTOR = (By.XPATH, ".//p[contains(text(),'Конструктор')]")
    BUTTON_ORDER_FEED = (By.XPATH, ".//p[contains(text(),'Лента Заказов')]")

    BUTTON_ORDER = (By.XPATH, ".//button[contains(text(),'заказ')]")

    @staticmethod
    def get_random_component_locator(random_component):
        random_component = By.XPATH, (f".//a[contains(@href, '"
                                      f"{random_component.get_attribute('href')[len(data.MAIN_URL):]}')]")
        return random_component
