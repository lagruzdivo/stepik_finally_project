from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket") # селектор кнопки добавления в корзину
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success:first-child") # сообщение, что товар добавлен в корзину
    PRODUCT_NAME_IN_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div strong") # что именно эта книга указана в сообщении
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    BASKET_TOTAL = (By.CSS_SELECTOR, ".alert-info strong") # цена указанная в сообщении стоимости корзины
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color") # цена у товара

