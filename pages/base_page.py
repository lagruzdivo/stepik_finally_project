from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.wait import WebDriverWait
from .locators import BasePageLocators, BasketPageLocators
import math


class BasePage():
    def __init__(self, browser, url, timeout=10): # конструктор, который вызывается когда создаем объект
        self.browser = browser
        self.url = url

    def go_to_login_page(self):
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()

    def go_to_basket_page(self): #Переходит в корзину по кнопке в шапке сайта
        link = self.browser.find_element(*BasketPageLocators.BASKET_BUTTON)
        link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"
        # проверяем что есть ссылка, которая ведёт на логин

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented" \
                                                                     " probably unauthorised user"

    def open(self): # открывает нужную страницу в браузере
        self.browser.get(self.url)

    def is_element_present(self, how, what): # для перехвата исключений
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True
