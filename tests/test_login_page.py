import allure

from pages.login_page import LoginPage


class TestLoginPage:
    @allure.title('Переход на страницу восстановления пароля по кнопке «Восстановить пароль»')
    @allure.description('При клике по кнопке "Восстановить пароль" осуществляется переход на страницу восстановления '
                        'пароля')
    def test_click_on_button_forgot_password(self, drivers):
        login_page = LoginPage(drivers)
        login_page.open()

        login_page.click_on_button_forgot_password()

        login_page.check_is_it_forgot_password_page()
