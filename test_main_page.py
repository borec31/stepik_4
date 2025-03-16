from pages.base_page import BasePage
from pages.basket_page import BasketPage


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    # Открываем главную страницу
    link = "http://selenium1py.pythonanywhere.com/"
    page = BasePage(browser, link)
    page.open()

    # Переходим в корзину
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)

    # Проверки
    basket_page.should_not_see_products_in_basket()
    basket_page.should_see_empty_basket_message()



# from .pages.main_page import MainPage
#
#
# def test_guest_can_go_to_login_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/"
#     page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
#     page.open()                      # открываем страницу
#     page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина


