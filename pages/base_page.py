from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        """Открытие страницы"""
        self.browser.get(self.url)

    def go_to_basket(self):
        """Переход в корзину по кнопке в шапке"""
        basket_link = self.browser.find_element(By.CSS_SELECTOR, ".basket-mini a.btn")
        basket_link.click()



# class BasePage():
#     def go_to_login_page(self):
#         link = self.browser.find_element(*BasePageLocators.LOGIN_LINK_INVALID)
#         link.click()
#
#     def should_be_login_link(self):
#         assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

