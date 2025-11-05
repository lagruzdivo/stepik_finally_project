from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.url

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "There is no login form"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "There is no register form"

    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.EMAIL_INPUT) # поиск поля емайл
        email_field.send_keys(email) # заполнение поля емайл

        password_field = self.browser.find_element(*LoginPageLocators.PASSWORD_INPUT) # поиск поля пароля
        password_field.send_keys(password) # заполнение поля пароля

        double_password_field = self.browser.find_element(*LoginPageLocators.DOUBLE_PASSWORD_INPUT) # поиск поля 2 пароля
        double_password_field.send_keys(password) # заполнение поля 2 пароля

        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON) # поиск кнопки регистрации
        register_button.click() # нажатие кнопки регистрации
