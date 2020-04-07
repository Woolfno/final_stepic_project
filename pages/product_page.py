from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    MESSAGE_SUCCESS_PRODUCT_ADD = "<strong>{product}</strong> has been added to your basket."
    
    def add_product_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        add_button.click()
        self.solve_quiz_and_get_code()

    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def get_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def should_be_message_add_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_ADD_TO_BASKET), "Messsage about add product is not present"

        message = self.browser.find_element(*ProductPageLocators.MESSAGE_ADD_TO_BASKET).get_attribute("innerHTML").strip()        
        assert self.__class__.MESSAGE_SUCCESS_PRODUCT_ADD.format(product=self.get_product_name())==message, "Product does not in message"

    def should_be_message_amount_basket(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_AMOUNT_BASKET), "Message about amount basket is not present"

        amount = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL).text
        assert self.get_price()==amount, "The cost of the basket does not match the price of the product"