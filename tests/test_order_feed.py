import allure

from pages.account_page import AccountPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.order_feed import OrderFeed


class TestOrderFeed:
    @allure.title('Проверка отображения деталей случайного заказа')
    @allure.description('При клике по иконке случайного заказа отображаются детали заказа')
    def test_click_on_order(self, drivers):
        order_page = OrderFeed(drivers)
        order_page.open()

        order_page.click_on_random_order()

        order_page.check_is_order_details_opened()

    @allure.title('Проверка отображения заказов пользователя в ленте')
    @allure.description('Недавно оформленный заказ отображается в ленте заказов')
    def test_is_placed_order_in_feed(self, drivers, email_and_password_of_account_with_an_order):
        account_page = AccountPage(drivers)
        order_feed = OrderFeed(drivers)

        email, password = email_and_password_of_account_with_an_order
        account_page.go_to_account_history(email, password)

        order_number = account_page.get_order_number()

        order_feed.open()

        order_feed.check_is_order_in_feed(order_number)

    @allure.title('Проверка увеличения счетчика заказов за все время')
    @allure.description('Счетчик заказов за все время увеличивается при оформлении заказа')
    def test_increase_total_order_counter(self, drivers, email_and_password_of_account_with_an_order):
        order_feed = OrderFeed(drivers)
        main_page = MainPage(drivers)
        login_page = LoginPage(drivers)

        order_feed.open()
        order_quantity = order_feed.get_total_order_number()

        email, password = email_and_password_of_account_with_an_order
        login_page.login(email, password)
        main_page.place_random_order()

        order_feed.open()
        new_order_quantity = order_feed.get_total_order_number()

        order_feed.check_is_counter_increased(new_order_quantity, order_quantity)

    @allure.title('Проверка увеличения счетчика заказов за сегодня')
    @allure.description('Счетчик заказов за сегодня увеличивается при оформлении заказа')
    def test_increase_today_order_counter(self, drivers, email_and_password_of_account_with_an_order):
        order_feed = OrderFeed(drivers)
        main_page = MainPage(drivers)
        login_page = LoginPage(drivers)

        order_feed.open()
        order_quantity = order_feed.get_today_order_number()

        email, password = email_and_password_of_account_with_an_order
        login_page.login(email, password)
        main_page.place_random_order()

        order_feed.open()
        new_order_quantity = order_feed.get_today_order_number()

        order_feed.check_is_counter_increased(new_order_quantity, order_quantity)

    @allure.title('Проверка добавления заказа в готовку')
    @allure.description('После оформления заказа его номер появляется в разделе В работе')
    def test_is_order_cooking(self, drivers, email_and_password_of_account_with_an_order):
        order_feed = OrderFeed(drivers)
        main_page = MainPage(drivers)
        login_page = LoginPage(drivers)
        email, password = email_and_password_of_account_with_an_order

        login_page.login(email, password)
        main_page.place_random_order()
        order_number = main_page.get_order_number()

        order_feed.open()

        order_feed.check_is_order_cooking(order_number)
