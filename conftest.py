import pytest
from faker import Faker
from selenium import webdriver

from api_modules.delete_user import DeleteUser
from api_modules.register_user import RegisterUser

fake = Faker(locale='ru_RU')


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(params=['chrome', 'firefox'])
def drivers(request):
    browser = None
    if request.param == 'chrome':
        browser = webdriver.Chrome()
    elif request.param == 'firefox':
        browser = webdriver.Firefox()

    yield browser
    browser.quit()


@pytest.fixture
def random_email():
    email = fake.email()
    return email


@pytest.fixture
def email_and_password():
    email = fake.email()
    password = fake.password()
    payload = {
        "email": email,
        "password": password,
        "name": fake.user_name()
    }

    create_user = RegisterUser()
    create_user.create_user(payload)
    access_token = create_user.get_access_token()

    yield email, password

    DeleteUser().delete_user(access_token)
