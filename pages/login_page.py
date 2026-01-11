from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        current_url = self.browser.current_url
        assert "login" in current_url, f"There is no a login URL"

    def should_be_login_form(self):
        assert (self.is_element_present(*LoginPageLocators.LOGIN_USER_NAME) and
                self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD)), "The login form isn't on the page"

    def should_be_register_form(self):
        assert (self.is_element_present(*LoginPageLocators.REGISTER_EMAIL) and
                self.is_element_present(*LoginPageLocators.REGISTER_PASSWORD_1) and
                self.is_element_present(*LoginPageLocators.REGISTER_PASSWORD_2)), "The register form isn't on the page"

    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        email_field.send_keys(email)
        password_field_1 = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_1)
        password_field_1.send_keys(password)
        password_field_2 = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_2)
        password_field_2.send_keys(password)
        reg_button = WebDriverWait(self.browser, 10).until(
            ec.element_to_be_clickable(LoginPageLocators.REGISTRATION_BUTTON),
            "Кнопка регистрации не найдена"
        )
        reg_button.click()
        self.should_be_authorized_user()
