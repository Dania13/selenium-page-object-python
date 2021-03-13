from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    EMAIL_REGISTER = (By.CSS_SELECTOR, '#id_registration-email')
    PASSWORD_REGISTER = (By.CSS_SELECTOR, '#id_registration-password1')
    CONFIRM_PASSWORD_REGISTER = (By.CSS_SELECTOR, '#id_registration-password2')
    REGISTER_BUTTON = (By.XPATH, "//button[@name='registration_submit']")


class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, '.btn-add-to-basket')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main h1')
    PRODUCT_NAME_MESSAGE = (
        By.CSS_SELECTOR, '#messages div.alert:nth-child(1) strong')
    PRODUCT_PRICE_MESSAGE = (
        By.CSS_SELECTOR, '#messages div.alert:nth-child(3) strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#messages div.alert')


class BasePageLocators():
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group a")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators():
    BASKET_EMPTY = (By.CSS_SELECTOR, '#content_inner > p')
