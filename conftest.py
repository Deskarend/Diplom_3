import pytest
import requests
from faker import Faker
from selenium import webdriver

fake = Faker(locale='ru_RU')


@pytest.fixture(params=['chrome', 'firefox'])
def drivers(request):
    browser = None
    if request.param == 'chrome':
        browser = webdriver.Chrome()
    elif request.param == 'firefox':
        browser = webdriver.Firefox()
    browser.maximize_window()
    yield browser
    browser.quit()


@pytest.fixture
def email_and_password_of_account_with_an_order():
    email = fake.email()
    password = fake.password()
    payload = {
        "email": email,
        "password": password,
        "name": fake.user_name()
    }
    burger = {
        "ingredients": ["61c0c5a71d1f82001bdaaa74", "61c0c5a71d1f82001bdaaa6e", "61c0c5a71d1f82001bdaaa7a",
                        "61c0c5a71d1f82001bdaaa76", "61c0c5a71d1f82001bdaaa6d"]
    }

    base_url = 'https://stellarburgers.nomoreparties.site/'
    register_endpoint = 'api/auth/register'
    delete_endpoint = 'api/auth/user'
    order_endpoint = 'api/orders'

    account = requests.post(base_url + register_endpoint, payload)
    token = account.json().get('accessToken')

    requests.post(base_url + order_endpoint, burger, headers={"Authorization": token})

    yield email, password

    requests.delete(base_url + delete_endpoint, headers={"Authorization": token})
