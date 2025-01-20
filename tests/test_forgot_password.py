import allure
from faker import Faker

from pages.forgot_password_page import ForgotPassword

fake = Faker(locale='ru_RU')


class TestForgotPassword:
    @allure.title('Переход на форму восстановления пароля по кнопке «Восстановить»')
    @allure.description('При вводе почты и клике по кнопке "Восстановить" осуществляется переход на форму '
                        'восстановления пароля ')
    def test_click_on_button_reset(self, drivers, random_email):
        forgot_password = ForgotPassword(drivers)
        forgot_password.open()

        forgot_password.set_email(random_email)
        forgot_password.click_on_button_reset()

        forgot_password.check_is_it_reset_password_form()

    @allure.title('Клик по кнопке показать/скрыть пароль подсвечивает его')
    @allure.description('Клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его')
    def test_click_on_button_show_or_hide_password(self, drivers, random_email):
        forgot_password = ForgotPassword(drivers)
        forgot_password.go_to_form_reset_password(random_email)

        forgot_password.click_on_button_show_or_hide_password()

        forgot_password.check_is_field_password_focused()
