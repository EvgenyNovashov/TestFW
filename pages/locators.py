from selenium.webdriver.common.by import By

class BasePageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.CSS_SELECTOR, ".basket-mini a.btn.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class MainPageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators(object):
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_PASSWORD_REP = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "#register_form button")
    LOGIN_WORD = 'login'


class ProductPageLocators(object):
    BUTTON_ADD_CARD = (By.CSS_SELECTOR, "#add_to_basket_form > button")
    PRODUCT = (By.CSS_SELECTOR, ".col-sm-6.product_main h1")
    PRODUCT_ADD_CARD = (By.CSS_SELECTOR, "#messages strong")
    PRODUCT_COST = (By.CSS_SELECTOR, ".col-sm-6.product_main p")
    COST_ADD_CARD = (By.CSS_SELECTOR, ".alert.alert-safe.alert-noicon.alert-info strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div")

class BasketPageLocators(object):
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")
    BASKET_MESSAGE_EMPTY = (By.CSS_SELECTOR, "#content_inner p")

