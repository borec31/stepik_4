from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_not_see_products_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "Basket contains products, but it should be empty"
    
    def should_see_empty_basket_message(self):
        assert self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_MESSAGE).text == "Your basket is empty.", \
            "Empty basket message is not present or incorrect"

