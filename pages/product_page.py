from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def go_to_basket(self):
        add_to_basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_to_basket.click()

    def should_by_basket_page(self):
        # Удаление всех куки
        self.browser.delete_all_cookies()
        # Очистка локального хранилища
        self.browser.execute_script("window.localStorage.clear();")
        # Очистка сессионного хранилища
        self.browser.execute_script("window.sessionStorage.clear();")
        self.should_be_add_to_basket()
        self.should_be_valid_price()

    def should_be_add_to_basket(self):
        name_in_page = WebDriverWait(self.browser, 10).until(
            ec.visibility_of_element_located(ProductPageLocators.NAME_IN_PAGE)).text
        name_in_basket = WebDriverWait(self.browser, 10).until(
            ec.visibility_of_element_located(ProductPageLocators.NAME_IN_BASKET)).text
        assert name_in_page == name_in_basket, "\nWarning: No adding product into basket"

    def should_be_valid_price(self):
        price_in_page = self.browser.find_element(*ProductPageLocators.PRICE_IN_PAGE).text
        prices_in_basket = self.browser.find_elements(*ProductPageLocators.PRICE_IN_BASKET)
        price_in_basket = prices_in_basket[0].text
        assert price_in_page == price_in_basket, "\nWarning: The product price is not valid!"
