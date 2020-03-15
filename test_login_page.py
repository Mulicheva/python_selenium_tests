from .pages.login_page import LoginPage

def test_guest_can_see_login_in_url(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = LoginPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    page.should_be_login_page()          # выполняем метод страницы - переходим на страницу логина


