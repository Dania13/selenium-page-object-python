from pages.locators import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # http://selenium1py.pythonanywhere.com/ru/accounts/login/
        # реализуйте проверку на корректный url адрес
        assert self.current_url().find("login") != -1, "Login URL is not correct"

    def should_be_login_form(self):
        # проверка, что есть форма логина
        assert self.is_element_present(
            *LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # проверка, что есть форма регистрации на странице
        assert self.is_element_present(
            *LoginPageLocators.REGISTER_FORM), "Register form is not presented"