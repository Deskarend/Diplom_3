from selenium.webdriver.common.by import By

from locators.base_page_locators import BasePageLocators


class OrderFeedPageLocators(BasePageLocators):
    ORDER_FEED = (By.XPATH, ".//div[contains(@class, 'orderFeed')]")

    ORDERS = (By.XPATH, ".//a[contains(@href, '/feed/')]")
    ORDER_DETAILS = (By.XPATH, ".//section[contains(@class, 'opened')]//div[contains(@class, 'orderBox')]")

    ORDER_NUMBERS = (By.XPATH, ".//div[contains(@class, 'textBox')]//p[contains(@class, 'digits')]")

    TOTAL_ORDER_COUNTER = (By.XPATH, ".//p[contains(text(), 'за все время')]/following-sibling::p")
    TODAY_ORDER_COUNTER = (By.XPATH, ".//p[contains(text(), 'за сегодня')]/following-sibling::p")

    IN_COOKING_LIST = (By.XPATH, ".//ul[contains(@class, 'ListReady')]")
    EMPTY_COOKING_LIST = (By.XPATH, ".//li[contains(text(), 'заказы готовы')]")