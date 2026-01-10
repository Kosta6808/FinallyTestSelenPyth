import pytest

from .pages.main_page import MainPage
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage


@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param(
                                      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                      marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
class TestsProductPage:

    def test_guest_can_add_product_to_basket(self, browser, link):
        page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        product_page = ProductPage(browser, link)
        product_page.go_to_basket()  # выполняем метод страницы — добавляем продукт в корзину
        product_page.solve_quiz_and_get_code()  # Выполняем условие доступа на basket page
        product_page.should_by_basket_page()

    @pytest.mark.xfail
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser, link):
        page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        product_page = ProductPage(browser, link)
        product_page.go_to_basket()  # выполняем метод страницы — добавляем продукт в корзину
        product_page.solve_quiz_and_get_code()  # Выполняем условие доступа на basket page
        product_page.should_not_be_success_message()

    def test_guest_cant_see_success_message(self, browser, link):
        page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        product_page = ProductPage(browser, link)
        product_page.should_not_be_success_message()

    @pytest.mark.skip
    def test_message_disappeared_after_adding_product_to_basket(self, browser, link):
        page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        product_page = ProductPage(browser, link)
        product_page.go_to_basket()  # выполняем метод страницы — добавляем продукт в корзину
        product_page.solve_quiz_and_get_code()  # Выполняем условие доступа на basket page
        product_page.should_disappeared()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    basket_page = BasketPage(browser, link)
    basket_page.open()
    basket_page.go_to_basket()
    basket_page.control_basket()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.go_to_login_page()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_be_login_link()
