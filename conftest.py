import pytest
from selenium import webdriver


@pytest.fixture(params=['chrome', 'firefox'])
def drivers(request):
    browser = None
    if request.param == 'chrome':
        browser = webdriver.Chrome()
    elif request.param == 'firefox':
        browser = webdriver.Firefox()
    yield browser
    browser.quit()
