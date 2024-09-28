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
