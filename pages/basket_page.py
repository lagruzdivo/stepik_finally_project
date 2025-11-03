from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_be_empty_basket(self): # проверяем что корзина пуста
        self.should_not_be_products() # Проверяем что нет товаров
        self.should_be_empty_basket_message() # Проверяем что есть сообщение о пустой корзине

    def should_not_be_products(self):
        # Проверяет что в корзине нет товаров (отрицательная проверка)
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "Basket is not empty, but should be!"

    def should_be_empty_basket_message(self):
        # Проверяет что есть сообщение о пустой корзине
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), "Empty basket message is not presented"