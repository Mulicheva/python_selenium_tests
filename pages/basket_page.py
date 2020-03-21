from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def  basket_should_be_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_FORMSET),'Basket not empty'


    def should_be_text_about_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_TEXT), "Text about empty basket is not presented"
