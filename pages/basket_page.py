from .base_page import BasePage
from .locators import BasketLocators


class BasketPage(BasePage):
    def should_be_empty(self):
        assert self.is_not_element_present(*BasketLocators.BASKET_ITEMS),\
            'Basket is not empty'

    def should_be_message_about_empty_basket(self):        
        assert self.is_element_present(*BasketLocators.MESSAGE_EMPTY_BASKET),\
            'Message about empty basket is not present'
        
        message = self.browser.find_element(*BasketLocators.MESSAGE_EMPTY_BASKET).text
        assert "Your basket is empty." in message,\
            'Message about empty basket is not correct'