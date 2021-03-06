import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--browser_name',\
                     action='store',\
                     default='chrome',\
                     help='Choose browser: chrome')
    parser.addoption('--language', \
                     action='store', \
                     default="en", \
                     help='Choose language: ru, en, ...(etc.)')

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption('browser_name')
    user_language = request.config.getoption('language')
    if (browser_name=='chrome'):
        print("\nstart browser for test..")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        #browser = webdriver.Chrome("C:/chromedriver/chromedriver.exe", options=options)
        browser = webdriver.Chrome(options=options)
    else:
        print("\nBrowser <browser_name> still is not implemented")
    yield browser
    print("\nquit browser..")
    browser.quit()