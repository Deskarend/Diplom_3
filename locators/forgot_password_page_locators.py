from selenium.webdriver.common.by import By

from locators.base_page_locators import BasePageLocators


class ForgotPasswordPageLocators(BasePageLocators):
    BUTTON_RESET = (By.XPATH, './/button[contains(text(),"Восстановить")]')
    FIELD_EMAIL = (By.XPATH, './/label[contains(text(),"Email")]/following-sibling::input')

    FIELD_NEW_PASSWORD = (By.XPATH, './/input[contains(@name,"пароль")]')
    FIELD_NEW_PASSWORD_IS_FOCUSED = (By.XPATH, './/div[contains(@class, "status_active")]')
    FIELD_EMAIL_CODE = (By.XPATH, './/label[contains(text(),"код")]/following-sibling::input')

    BUTTON_SHOW_OR_HIDE_PASSWORD = (By.XPATH, './/div[contains(@class, "icon-action")]')