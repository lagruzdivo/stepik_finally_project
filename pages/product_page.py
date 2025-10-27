from .base_page import BasePage
from .locators import ProductPageLocators



class ProductPage(BasePage):
    def add_to_basket(self):  #  метод добавления в корзину
        button_add_to_basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        button_add_to_basket.click() # клик добавить в корзину
        self.solve_quiz_and_get_code()  # обработка промо-аллерта ПОСЛЕ добавления

    def should_be_add_success_message(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "There is no success message"

    def should_be_correct_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_name_in_message = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_MESSAGE).text
        assert product_name == product_name_in_message, "The product name don't match"


    def should_be_correct_basket_total(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        basket_total = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL).text
        assert product_price == basket_total, "The basket total is incorrect"