from pages.main_page import MainPage
from pages.basket_page import BasketPage

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = MainPage(browser)
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_see_products_in_basket()
    basket_page.should_see_empty_basket_message()
