from selenium.webdriver.common.by import By

from locators.base_page_locators import BasePageLocators


class LoginPageLocators(BasePageLocators):
    BUTTON_FORGOT_PASSWORD = (By.XPATH, ".//a[contains(@href,'/forgot-password')]")

    INPUT_EMAIL = (By.XPATH, ".//input[@name='name']")
    INPUT_PASSWORD = (By.XPATH, ".//input[@name='Пароль']")
    BUTTON_LOGIN = (By.XPATH, ".//button[contains(text(), 'Войти')]")