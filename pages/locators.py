from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_URL = (By.CSS_SELECTOR, '#login_link')
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, '.btn-add-to-basket')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main>h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main>p.price_color')
    MASSAGE_ABOUT_SUCCESS_ADD_TO_BUSKED = (By.CSS_SELECTOR, '#messages>.alert:nth-child(1)>.alertinner>strong')
    MASSEGE_ABOUT_BUSKED_PRICE = (By.CSS_SELECTOR, '.alert-info>.alertinner>p>strong')
