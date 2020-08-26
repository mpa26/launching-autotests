import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# run command: pytest --language=es test_items.py
def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: es or ru")


@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)
    yield browser
    time.sleep(5)
    print("\nquit browser..")
    browser.quit()

