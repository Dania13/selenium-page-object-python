from pages.locators import BasketPageLocators
from pages.base_page import BasePage


class BasketPage(BasePage):

    def should_be_basket_page(self):
        self.should_be_basket_url()

    def should_be_basket_url(self):
        assert self.url.find("basket") != -1, "Basket URL is not correct"

    def should_not_have_things_in_basket(self):
        assert self.browser.find_element(
            *BasketPageLocators.BASKET_EMPTY), "Basket is not empty, but should be"

    def should_message_is_about_empty_basket(self, language):
        text_of_empty_basket = {
            "ar": "سلة التسوق فارغة متابعة التسوق",
            "ca": "La seva cistella està buida. Continua les seves compres",
            "cs": "Váš košík je prázdný. Pokračovat v nakupování",
            "da": "Din indkøbskurv er tom. Køb mere",
            "de": "Ihr Warenkorb ist leer. Einkauf fortsetzen",
            "en": "Your basket is empty. Continue shopping",
            "en-US": "Your basket is empty. Continue shopping",
            "el": "Το καλάθι σας είναι άδειο. Συνεχίστε τις αγορές σας",
            "es": "Tu carrito esta vacío. Continuar sus compras",
            "fi": "Korisi on tyhjä Jatka ostoksia",
            "fr": "Votre panier est vide. Continuer ses achats",
            "it": "Il tuo carrello è vuoto. Continua lo shopping",
            "ko": "장바구니가 비었습니다. 쇼핑 계속하기",
            "nl": "Je winkelmand is leeg Verdergaan met winkelen",
            "pl": "Twój koszyk jest pusty. Kontynuuj zakupy",
            "pt": "O carrinho está vazio. Continuar a comprar",
            "pt-br": "Sua cesta está vazia. Continuar comprando",
            "ro": "Cosul tau este gol. Continua cumparaturile",
            "ru": "Ваша корзина пуста Продолжить покупки",
            "sk": "Váš košík je prázdny Pokračovať v nákupe",
            "uk": "Ваш кошик пустий. Продовжити покупки",
            "zh-cn": "Your basket is empty. Continue shopping",
        }

        basket_empty = self.browser.find_element(
            *BasketPageLocators.BASKET_EMPTY)
        assert basket_empty.text == text_of_empty_basket[language],\
            f"text of basket empty is {basket_empty.text},\
             but should be {text_of_empty_basket[language]}"
