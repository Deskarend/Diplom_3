import allure

from pages.account_page import AccountPage


class TestAccountPage:
    @allure.title('Переход в историю заказов в «Личный кабинет»')
    @allure.description('При клике по истории заказов в "Личный кабинет" осуществляется переход в раздел история '
                        'заказов')
    def test_turn_order_history(self, drivers, email_and_password_of_account_with_an_order):
        account_page = AccountPage(drivers)
        email, password = email_and_password_of_account_with_an_order
        account_page.go_to_account(email, password)

        account_page.click_on_order_history()

        account_page.check_is_it_order_history()

    @allure.title('Выход из аккаунта')
    @allure.description('При клике по кнопке "Выход" в "Личный кабинет" осуществляется переход на страницу авторизации')
    def test_exit_from_account(self, drivers, email_and_password_of_account_with_an_order):
        account_page = AccountPage(drivers)
        email, password = email_and_password_of_account_with_an_order
        account_page.go_to_account(email, password)

        account_page.click_on_exit_button()

        account_page.check_is_it_login_page()

    @allure.title('Проверка перехода по кнопке конструктора')
    @allure.description('При клике по кнопке "Конструктор" в "Личный кабинет" осуществляется переход на главную '
                        'страницу')
    def test_click_on_button_constructor(self, drivers, email_and_password_of_account_with_an_order):
        account_page = AccountPage(drivers)
        email, password = email_and_password_of_account_with_an_order
        account_page.go_to_account(email, password)

        account_page.click_on_button_constructor()

        account_page.check_is_it_main_page()

    @allure.title('Проверка перехода по кнопке ленты заказов')
    @allure.description('При клике по кнопке "Лента Заказов" в "Личный кабинет" осуществляется переход на страницу '
                        'ленты заказов')
    def test_click_on_button_order_feed(self, drivers, email_and_password_of_account_with_an_order):
        account_page = AccountPage(drivers)
        email, password = email_and_password_of_account_with_an_order
        account_page.go_to_account(email, password)

        account_page.click_on_button_order_feed()

        account_page.check_is_it_order_feed_page()
