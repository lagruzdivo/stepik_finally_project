from selenium.webdriver.common.by import By

class MainPageLocators():
    pass

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_INPUT = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "#id_registration-password1")
    DOUBLE_PASSWORD_INPUT = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "button[name='registration_submit']")


class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket") # селектор кнопки добавления в корзину
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success:first-child") # сообщение, что товар добавлен в корзину
    PRODUCT_NAME_IN_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div strong") # что именно эта книга указана в сообщении
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    BASKET_TOTAL = (By.CSS_SELECTOR, ".alert-info strong") # цена указанная в сообщении стоимости корзины
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color") # цена у товара

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, '.btn-group .btn-default:first-child')

    # Блоки с товарами в корзине (проверить в браузере)
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items") # Элементы товаров в корзине

    # Сообщение "Ваша корзина пуста" (проверить в браузере)
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner > p") # Сообщение "Ваша корзина пуста"

