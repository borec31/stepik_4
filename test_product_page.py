import pytest
from pages.product_page import ProductPage
from pages.basket_page import BasketPage


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    # Открываем страницу товара
    page = ProductPage(browser)
    page.open()

    # Переходим в корзину
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)

    # Проверки
    basket_page.should_not_see_products_in_basket()
    basket_page.should_see_empty_basket_message()


# Существующие тесты (оставляем для примера)
@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser)
    page.open()
    page.add_product_to_basket()
    assert page.is_not_element_present(*ProductPage.SUCCESS_MESSAGE), "Success message is present after adding product"


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser)
    page.open()
    assert page.is_not_element_present(*ProductPage.SUCCESS_MESSAGE), "Success message is present on page load"


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser)
    page.open()
    page.add_product_to_basket()
    assert page.is_disappeared(*ProductPage.SUCCESS_MESSAGE), "Success message did not disappear after adding product"






# from pages.product_page import ProductPage
#
#
# def test_guest_can_add_product_to_basket(browser):
#     # URL страницы с промо-кодом
#     link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
#
#     # Инициализация страницы
#     page = ProductPage(browser)
#     browser.get(link)
#
#     # Выполнение действий и проверок
#     page.add_product_to_basket()
#     page.should_be_success_message()
#     page.should_be_correct_product_name_in_message()
#     page.should_be_correct_basket_total()

# from pages.product_page import ProductPage
#
#
# def test_guest_can_add_product_to_basket(browser):
#     # Новая ссылка из задания
#     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
#
#     # Инициализация страницы
#     page = ProductPage(browser)
#     browser.get(link)
#
#     # Выполнение действий и проверок
#     page.add_product_to_basket()
#     page.should_be_success_message()
#     page.should_be_correct_product_name_in_message()
#     page.should_be_correct_basket_total()


# import pytest
# from pages.product_page import ProductPage
#
#
# @pytest.mark.parametrize('link', [
#     "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#     "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#     "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#     "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#     "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#     "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#     "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#     "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
#     "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#     "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
# ])
# def test_guest_can_add_product_to_basket(browser, link):
#     # Инициализация страницы
#     page = ProductPage(browser)
#     browser.get(link)
#
#     # Выполнение действий и проверок
#     page.add_product_to_basket()
#     page.should_be_success_message()
#     page.should_be_correct_product_name_in_message()
#     page.should_be_correct_basket_total()



# import pytest
# from pages.product_page import ProductPage
#
# link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
#
# @pytest.mark.xfail
# def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
#     page = ProductPage(browser)
#     browser.get(link)
#     page.add_product_to_basket()
#     assert page.is_not_element_present(*ProductPage.SUCCESS_MESSAGE), "Success message is present after adding product"
#
# def test_guest_cant_see_success_message(browser):
#     page = ProductPage(browser)
#     browser.get(link)
#     assert page.is_not_element_present(*ProductPage.SUCCESS_MESSAGE), "Success message is present on page load"
#
# @pytest.mark.xfail
# def test_message_disappeared_after_adding_product_to_basket(browser):
#     page = ProductPage(browser)
#     browser.get(link)
#     page.add_product_to_basket()
#     assert page.is_disappeared(*ProductPage.SUCCESS_MESSAGE), "Success message did not disappear after adding product"
#
# def test_guest_should_see_login_link_on_product_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
#     page = ProductPage(browser, link)
#     page.open()
#     page.should_be_login_link()


