from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def control_basket(self):
        self.control_quantity_product_in_basket()
        self.control_text_empty_basket()

    def control_text_empty_basket(self):
        # div#content_inner p  контроль сообщения о пустоте корзины
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET), "The message about empty basket is absent"

    def control_quantity_product_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.QUANTITY_PRODUCTS), "The basket is not empty"
