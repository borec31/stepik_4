from .base_page import BasePage

class MainPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser, "http://selenium1py.pythonanywhere.com/")
