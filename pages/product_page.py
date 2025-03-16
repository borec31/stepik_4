from selenium.common.exceptions import NoAlertPresentException
import math
from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser, "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0")
    
    def add_product_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN).click()
        self.solve_quiz_and_get_code()
    
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
    
    def should_be_success_message(self):
        assert self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is not presented"
    
    def should_be_correct_product_name_in_message(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        message = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text
        assert product_name in message, f"Expected product name '{product_name}' not found in message: '{message}'"
    
    def should_be_correct_basket_total(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        basket_total = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL).text
        assert product_price == basket_total, f"Basket total '{basket_total}' doesn't match product price '{product_price}'"


