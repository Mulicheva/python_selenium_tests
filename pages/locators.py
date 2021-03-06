from lib2to3.pgen2 import driver

from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET = (By.CSS_SELECTOR, "#default > header > div.page_inner > div > div.basket-mini.pull-right.hidden-xs > span > a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators ():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_USERNAME = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")
    REGISTER_EMAIL_ADDRESS = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_CONFIRM_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "#register_form button")
    LOGIN_SUBMIT =(By.CSS_SELECTOR, '[button name="login_submit"]')
class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    BOOK_NAME_MSG = (By.CSS_SELECTOR, '#messages > div:nth-child(1) > div > strong')
    BOOK_NAME = (By.CSS_SELECTOR, '#content_inner > article > div.row > div.col-sm-6.product_main > h1')
    BOOK_PRICE_MSG = (By.CSS_SELECTOR, '#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#messages > div:nth-child(1) > div > strong')
    BASKET_VALUE = (By.CSS_SELECTOR, '#content_inner > article > div.row > div.col-sm-6.product_main > p.price_color')

class BasketPageLocators():
    BASKET_FORMSET = (By.CSS_SELECTOR, '#basket_formset')
    EMPTY_BASKET_TEXT = (By.CSS_SELECTOR, '#content_inner > p ')
