from .base_page import BasePage
from .locators import BasketPageLocators

class CartPage(BasePage):
    def should_not_be_product_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "Basket include product"

    def should_be_message_basket_empty(self):
        basket_message = self.browser.find_element(*BasketPageLocators.BASKET_MESSAGE_EMPTY).text
        assert basket_message == 'Your basket is empty. Continue shopping', "Basket message is not empty"


