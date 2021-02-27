from pages.locators import ProductPageLocators
from pages.base_page import BasePage


class ProductPage(BasePage):
    def add_product_to_basket(self):
        btn_add_to_basket = self.browser.find_element(
            *ProductPageLocators.ADD_TO_BASKET)
        btn_add_to_basket.click()

    def should_be_product_add_to_basket(self):
        self.should_be_product_name_in_message()
        self.should_be_price_in_basket_equal_product_price()

    def should_be_product_name_in_message(self):
        # Сообщение о том, что товар добавлен в корзину. Название товара в сообщении должно совпадать с тем товаром, который вы действительно добавили.
        product_name_cart = self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME)
        product_name_message = self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME_MESSAGE)
        assert product_name_cart.text == product_name_message.text, "Name of product in message is not equal name of product in cart"

    def should_be_price_in_basket_equal_product_price(self):
        # Сообщение со стоимостью корзины. Стоимость корзины совпадает с ценой товара.
        product_price_cart = self.browser.find_element(
            *ProductPageLocators.PRODUCT_PRICE)
        product_price_message = self.browser.find_element(
            *ProductPageLocators.PRODUCT_PRICE_MESSAGE)
        assert product_price_cart.text == product_price_message.text, "Price of product in message is not equal price of product in cart"
