from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from .locators import BasePageLocators

class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
    
    def open(self):
        self.browser.get(self.url)
    
    def go_to_basket(self):
        self.browser.find_element(*BasePageLocators.BASKET_LINK).click()
    
    def go_to_login_page(self):
        self.browser.find_element(*BasePageLocators.LOGIN_LINK).click()
    
    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False
    
    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True
