from selenium.webdriver.common.by import By

from locators.base_page_locators import BasePageLocators


class MainPageLocators(BasePageLocators):
    BUTTON_ACCOUNT = (By.XPATH, ".//a[contains(@href, '/account')]")

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
    ORDER_NUMBER = (By.XPATH, ".//p[contains(text(), 'идентификатор')]/preceding-sibling::h2")
    NOT_UPLOADED_ORDER_NUMBER = (By.XPATH, ".//h2[contains(text(), '9999')]")
