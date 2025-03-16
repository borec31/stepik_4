from selenium.webdriver.common.by import By
from .base_page import BasePage


class BasketPage(BasePage):
    BASKET_ITEMS = (By.CSS_SELECTOR, "#basket_formset")
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner p")

    def should_not_see_products_in_basket(self):
        """Проверка, что в корзине нет товаров"""
        assert self.is_not_element_present(*self.BASKET_ITEMS), "Basket contains products, but it should be empty"

    def should_see_empty_basket_message(self):
        """Проверка, что есть текст о пустой корзине"""
        assert self.browser.find_element(*self.EMPTY_BASKET_MESSAGE).text == "Your basket is empty.", \
            "Empty basket message is not present or incorrect"

    def is_not_element_present(self, how, what, timeout=4):
        """Проверка отсутствия элемента"""
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        from selenium.common.exceptions import TimeoutException
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

