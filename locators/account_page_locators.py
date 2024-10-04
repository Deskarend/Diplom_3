from selenium.webdriver.common.by import By

from locators.base_page_locators import BasePageLocators


class AccountPageLocators(BasePageLocators):
    ACCOUNT_NAVIGATION = (By.XPATH, './/nav[contains(@class, "Account_nav")]')
    ORDER_HISTORY = (By.XPATH, ".//a[contains(@href, '/account/order-history')]")
    ORDER_HISTORY_ACTIVE = (By.XPATH, './/a[contains(@href,"/account/order-history") and contains(@class,'
                                      '"link_active")]')

    BUTTON_EXIT = (By.XPATH, ".//button[contains(text(), 'Выход')]")