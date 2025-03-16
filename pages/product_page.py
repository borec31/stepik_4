from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoAlertPresentException
import math
from .base_page import BasePage


class ProductPage(BasePage):
    ADD_TO_BASKET_BTN = (By.CSS_SELECTOR, "#add_to_basket_form button[type='submit']")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success .alertinner")
    BASKET_TOTAL = (By.CSS_SELECTOR, ".alert-info .alertinner strong")

    def __init__(self, browser):
        super().__init__(browser, "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0")

    def add_product_to_basket(self):
        add_button = self.browser.find_element(*self.ADD_TO_BASKET_BTN)
        add_button.click()
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

    def get_product_name(self):
        return self.browser.find_element(*self.PRODUCT_NAME).text

    def get_product_price(self):
        return self.browser.find_element(*self.PRODUCT_PRICE).text

    def should_be_success_message(self):
        assert self.browser.find_element(*self.SUCCESS_MESSAGE), "Success message is not presented"

    def should_be_correct_product_name_in_message(self):
        product_name = self.get_product_name()
        message = self.browser.find_element(*self.SUCCESS_MESSAGE).text
        assert product_name in message, f"Expected product name '{product_name}' not found in message: '{message}'"

    def should_be_correct_basket_total(self):
        product_price = self.get_product_price()
        basket_total = self.browser.find_element(*self.BASKET_TOTAL).text
        assert product_price == basket_total, f"Basket total '{basket_total}' doesn't match product price '{product_price}'"





# from selenium.webdriver.common.by import By
# import math
# from selenium.common.exceptions import NoAlertPresentException
#
#
# class ProductPage:
#     def __init__(self, browser):
#         self.browser = browser
#
#     # Локаторы
#     ADD_TO_BASKET_BTN = (By.CSS_SELECTOR, "#add_to_basket_form button[type='submit']")
#     PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
#     PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
#     SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success .alertinner")
#     BASKET_TOTAL = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
#
#     def add_product_to_basket(self):
#         """Добавление товара в корзину"""
#         add_button = self.browser.find_element(*self.ADD_TO_BASKET_BTN)
#         add_button.click()
#         self.solve_quiz_and_get_code()
#
#     def solve_quiz_and_get_code(self):
#         """Решение математической задачи и получение кода"""
#         alert = self.browser.switch_to.alert
#         x = alert.text.split(" ")[2]
#         answer = str(math.log(abs((12 * math.sin(float(x))))))
#         alert.send_keys(answer)
#         alert.accept()
#         try:
#             alert = self.browser.switch_to.alert
#             alert_text = alert.text
#             print(f"Your code: {alert_text}")
#             alert.accept()
#         except NoAlertPresentException:
#             print("No second alert presented")
#
#     def get_product_name(self):
#         """Получение названия товара"""
#         return self.browser.find_element(*self.PRODUCT_NAME).text
#
#     def get_product_price(self):
#         """Получение цены товара"""
#         return self.browser.find_element(*self.PRODUCT_PRICE).text
#
#     def should_be_success_message(self):
#         """Проверка наличия сообщения об успехе"""
#         assert self.browser.find_element(*self.SUCCESS_MESSAGE), "Success message is not presented"
#
#     def should_be_correct_product_name_in_message(self):
#         """Проверка корректности названия товара в сообщении"""
#         product_name = self.get_product_name()
#         message = self.browser.find_element(*self.SUCCESS_MESSAGE).text
#         assert product_name in message, f"Product name {product_name} not found in success message"
#
#     def should_be_correct_basket_total(self):
#         """Проверка корректности суммы корзины"""
#         product_price = self.get_product_price()
#         basket_total = self.browser.find_element(*self.BASKET_TOTAL).text
#         assert product_price == basket_total, f"Basket total {basket_total} doesn't match product price {product_price}"


# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import NoAlertPresentException, TimeoutException
# import math
#
#
# class ProductPage:
#     def __init__(self, browser):
#         self.browser = browser
#
#     # Локаторы
#     ADD_TO_BASKET_BTN = (By.CSS_SELECTOR, "#add_to_basket_form button[type='submit']")
#     PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
#     PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
#     SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success .alertinner")
#     BASKET_TOTAL = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
#
#     def add_product_to_basket(self):
#         """Добавление товара в корзину"""
#         add_button = self.browser.find_element(*self.ADD_TO_BASKET_BTN)
#         add_button.click()
#         self.solve_quiz_and_get_code()
#
#     def solve_quiz_and_get_code(self):
#         """Решение математической задачи и получение кода"""
#         alert = self.browser.switch_to.alert
#         x = alert.text.split(" ")[2]
#         answer = str(math.log(abs((12 * math.sin(float(x))))))
#         alert.send_keys(answer)
#         alert.accept()
#         try:
#             alert = self.browser.switch_to.alert
#             alert_text = alert.text
#             print(f"Your code: {alert_text}")
#             alert.accept()
#         except NoAlertPresentException:
#             print("No second alert presented")
#
#     def get_product_name(self):
#         """Получение названия товара со страницы"""
#         return self.browser.find_element(*self.PRODUCT_NAME).text
#
#     def get_product_price(self):
#         """Получение цены товара со страницы"""
#         return self.browser.find_element(*self.PRODUCT_PRICE).text
#
#     def should_be_success_message(self):
#         """Проверка наличия сообщения об успехе"""
#         assert self.browser.find_element(*self.SUCCESS_MESSAGE), "Success message is not presented"
#
#     def should_be_correct_product_name_in_message(self):
#         """Проверка, что название товара в сообщении совпадает с названием на странице"""
#         product_name = self.get_product_name()
#         message = self.browser.find_element(*self.SUCCESS_MESSAGE).text
#         assert product_name in message, f"Expected product name '{product_name}' not found in message: '{message}'"
#
#     def should_be_correct_basket_total(self):
#         """Проверка, что сумма корзины совпадает с ценой товара"""
#         product_price = self.get_product_price()
#         basket_total = self.browser.find_element(*self.BASKET_TOTAL).text
#         assert product_price == basket_total, f"Basket total '{basket_total}' doesn't match product price '{product_price}'"
#
#     def is_not_element_present(self, how, what, timeout=4):
#         """Проверка, что элемент не присутствует на странице"""
#         try:
#             WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
#         except TimeoutException:
#             return True
#         return False
#
#     def is_disappeared(self, how, what, timeout=4):
#         """Проверка, что элемент исчезает со страницы"""
#         try:
#             WebDriverWait(self.browser, timeout).until_not(EC.presence_of_element_located((how, what)))
#         except TimeoutException:
#             return False
#         return True




