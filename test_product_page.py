from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
import time
import pytest

@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()  # открыли страницу товара
    page.add_to_basket(should_solve_quiz=True)  # нажали кнопку ДОБАВТЬ В КОРЗИНУ
    time.sleep(5)
    page.should_be_add_success_message()
    page.should_be_correct_product_name()
    page.should_be_correct_basket_total()

@pytest.mark.xfail(reason="fixing this bug right now")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.xfail(reason="fixing this bug right now")
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_success_message_disappeared()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link() # проверяет наличие ссылки

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()  # переходит по ссылке логина

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()  # Открываем главную страницу
    page.go_to_basket_page()  # Переходим в корзину по кнопке в шапке
    # Создаем объект страницы корзины и проверяем что она пуста
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty_basket()

@pytest.mark.login_user
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        # Открываем страницу логина/регистрации
        login_link = "http://selenium1py.pythonanywhere.com/accounts/login/"
        page = LoginPage(browser, login_link)
        page.open()
        # Регистрируем пользователя
        email = str(time.time()) + "@fakemail.com"
        password = "zzaaqqww1"
        page.register_new_user(email, password)
        time.sleep(5)
        # Проверяем что пользователь залогинен
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()  # открыли страницу товара
        page.add_to_basket()  # нажали кнопку ДОБАВТЬ В КОРЗИНУ
        time.sleep(5)
        page.should_be_add_success_message()
        page.should_be_correct_product_name()
        page.should_be_correct_basket_total()