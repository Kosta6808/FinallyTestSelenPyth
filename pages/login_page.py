from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        current_url = self.browser.current_url.text
        assert "login" in current_url, f"The page URL isn't {LoginPageLocators.LOGIN_PAGE_URL}"
        # assert True

    def should_be_login_form(self):
        assert (self.is_element_present(*LoginPageLocators.LOGIN_USER_NAME) and
                self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD)), "The login form isn't on the page"
        # assert True

    def should_be_register_form(self):
        assert (self.is_element_present(*LoginPageLocators.REGISTER_EMAIL) and
                self.is_element_present(*LoginPageLocators.REGISTER_PASSWORD) and
                self.is_element_present(*LoginPageLocators.REGISTER_PASSWORD_2)), "The register form isn't on the page"
        # assert True
