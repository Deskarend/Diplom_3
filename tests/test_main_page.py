import allure

from pages.login_page import LoginPage
from pages.main_page import MainPage


class TestMainPage:
    @allure.title('Переход на страницу личного кабинета по кнопке «Личный кабинет»')
    @allure.description('При авторизации и  клике по кнопке "Личный кабинет" осуществляется переход на страницу '
                        'личного кабинета')
    def test_click_on_button_account(self, drivers, email_and_password_of_account_with_an_order):
        login_page = LoginPage(drivers)
        main_page = MainPage(drivers)
        email, password = email_and_password_of_account_with_an_order
        login_page.login(email, password)

        main_page.click_on_button_account()

        main_page.check_is_it_account_page()

    @allure.title('Проверка перехода по кнопке ленты заказов')
    @allure.description('При клике по кнопке "Лента Заказов" на главной странице осуществляется переход на страницу '
                        'ленты заказов')
    def test_click_on_button_order_feed(self, drivers):
        main_page = MainPage(drivers)
        main_page.open()

        main_page.click_on_button_order_feed()

        main_page.check_is_it_order_feed_page()

    @allure.title('Проверка отображения деталей случайного ингредиента')
    @allure.description('При клике по иконке случайного ингредиента отображаются детали ингредиента')
    def test_click_on_ingredient(self, drivers):
        main_page = MainPage(drivers)
        main_page.open()

        main_page.click_on_random_ingredient()

        main_page.check_is_ingredient_details_opened()

    @allure.title('Проверка закрытия деталей случайного ингредиента')
    @allure.description('При клике по крестику деталей случайного ингредиента окно закрывается')
    def test_close_ingredient_details(self, drivers):
        main_page = MainPage(drivers)
        main_page.open()

        main_page.click_on_random_ingredient()
        main_page.close_ingredient_detail()

        main_page.check_is_ingredient_details_closed()

    @allure.title('Проверка увеличения счетчика ингредиента')
    @allure.description('при добавлении ингредиента в заказ счётчик этого ингредиента увеличивается')
    def test_increase_ingredient_counter(self, drivers):
        main_page = MainPage(drivers)
        main_page.open()

        main_page.add_random_ingredient_on_order()

        main_page.check_is_ingredient_counter_increased()

    @allure.title('Проверка оформления заказа')
    @allure.description('Залогиненный пользователь может оформить заказ')
    def test_place_order(self, drivers, email_and_password_of_account_with_an_order):
        main_page = MainPage(drivers)
        login_page = LoginPage(drivers)
        email, password = email_and_password_of_account_with_an_order
        login_page.login(email, password)

        main_page.add_random_burger_on_order()
        main_page.click_on_button_place_order()

        main_page.check_is_order_confirmed()

    @allure.title('Проверка оформления заказа')
    @allure.description('Залогиненный пользователь может оформить заказ')
    def test_place_order(self, drivers, email_and_password_of_account_with_an_order):
        main_page = MainPage(drivers)
        login_page = LoginPage(drivers)
        email, password = email_and_password_of_account_with_an_order
        login_page.login(email, password)

        main_page.add_random_burger_on_order()
        main_page.click_on_button_place_order()

        main_page.check_is_order_confirmed()
