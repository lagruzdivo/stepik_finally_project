from selenium.webdriver.common.by import By
from .base_page import BasePage # импорт класса BasePage
from .locators import MainPageLocators

class MainPage(BasePage): # наследник класса BasePage - имеет доступ ко всем атрибутам BasePage
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()


    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
        # проверяем что есть ссылка, которая ведёт на логин
