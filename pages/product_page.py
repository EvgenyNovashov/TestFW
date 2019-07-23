from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException
import math

class ProductPage(BasePage):
    def add_to_card(self):
        buttun = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_CARD)
        buttun.click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            print("Your code: {}".format(alert.text))
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def should_be_message(self):
        message = self.browser.find_element(*ProductPageLocators.PRODUCT_ADD_CARD).text
        product = self.browser.find_element(*ProductPageLocators.PRODUCT).text
        assert message == product, "message incorect"

    def should_be_cost(self):
        message_cost = self.browser.find_element(*ProductPageLocators.COST_ADD_CARD).text
        product_cost = self.browser.find_element(*ProductPageLocators.PRODUCT_COST).text
        assert product_cost == message_cost, "cost incorect"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"