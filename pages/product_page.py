from selenium.webdriver.common.by import By

from .base_page import BasePage
from .locators import ProductPageLocators
class ProductPage(BasePage):

    def add_to_basket(self):
        if self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON):
            add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
            add_to_basket_button.click()
    def check_orders_messages(self):
        self.check_book_name_messages()
        self.check_price_of_book_equal_basket_value_messages()
    def check_book_name_messages(self):
        if self.is_element_present(*ProductPageLocators.BOOK_NAME_MSG):
           book_name_msg= self.browser.find_element(*ProductPageLocators.BOOK_NAME_MSG)
           book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME)
           assert book_name_msg.text==book_name.text, "Wrong book name message"
        else:
            print('Book name message not found')
    def check_price_of_book_equal_basket_value_messages(self):
        if self.is_element_present(*ProductPageLocators.BOOK_PRICE_MSG):
           book_price_msg= self.browser.find_element(*ProductPageLocators.BOOK_PRICE_MSG)
           basket_value = self.browser.find_element(*ProductPageLocators.BASKET_VALUE)
           assert book_price_msg.text==basket_value.text, "Wrong book price message"
        else:
            print('Book price message not found')
