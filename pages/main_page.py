from selenium.common.exceptions import NoAlertPresentException

from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
        try:
            alert = self.browser.switch_to.alert
            alert.accept()
        except NoAlertPresentException:
            print("\nNo alert in login page")

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
