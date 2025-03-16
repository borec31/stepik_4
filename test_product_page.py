import pytest
from pages.product_page import ProductPage
from pages.basket_page import BasketPage

@pytest.mark.need_review
def test_user_can_add_product_to_basket(browser):
    page = ProductPage(browser)
    page.open()
    page.add_product_to_basket()
    page.should_be_success_message()
    page.should_be_correct_product_name_in_message()
    page.should_be_correct_basket_total()

@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser)
    page.open()
    page.add_product_to_basket()
    page.should_be_success_message()
    page.should_be_correct_product_name_in_message()
    page.should_be_correct_basket_total()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser)
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_see_products_in_basket()
    basket_page.should_see_empty_basket_message()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser)
    page.open()
    page.go_to_login_page()

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser)
    page.open()
    page.add_product_to_basket()
    assert page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is present after adding product"

def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser)
    page.open()
    assert page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is present on page load"

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser)
    page.open()
    page.add_product_to_basket()
    assert page.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message did not disappear after adding product"
