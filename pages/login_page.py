from pages.locators import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.url.find("login") != -1, "Login URL is not correct"

    def should_be_login_form(self):
        assert self.is_element_present(
            *LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(
            *LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        email_field = self.browser.find_element(
            *LoginPageLocators.EMAIL_REGISTER)
        password_field = self.browser.find_element(
            *LoginPageLocators.PASSWORD_REGISTER)
        confirm_password_field = self.browser.find_element(
            *LoginPageLocators.CONFIRM_PASSWORD_REGISTER)
        register_btn = self.browser.find_element(
            *LoginPageLocators.REGISTER_BUTTON)
        email_field.send_keys(email)
        password_field.send_keys(password)
        confirm_password_field.send_keys(password)
        register_btn.click()
