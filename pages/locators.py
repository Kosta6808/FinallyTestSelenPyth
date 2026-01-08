from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_USER_NAME = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")
    REGISTER_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_PASSWORD_2 = (By.CSS_SELECTOR, "#id_registration-password2")


class ProductPageLocators:
    ADD_TO_BASKET = (By.CSS_SELECTOR, "button.btn.btn-add-to-basket")
    NAME_IN_PAGE = (By.CSS_SELECTOR, 'div.row h1')
    PRICE_IN_PAGE = (By.CSS_SELECTOR, "p.price_color")
    NAME_IN_BASKET = (By.CSS_SELECTOR, "div.alertinner strong")
    PRICE_IN_BASKET = (By.CSS_SELECTOR, "div.alertinner p strong")
