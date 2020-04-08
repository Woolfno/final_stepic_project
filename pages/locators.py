from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini a")
    USER_ICON = (By.CSS_SELECTOR, '.icon-user')

class BasketLocators:
    BASKET_ITEMS = (By.CLASS_NAME, 'basket-items')
    MESSAGE_EMPTY_BASKET = (By.CSS_SELECTOR, '#content_inner p')

class LoginPageLocators():
    LOGIN_FORM = (By.ID, 'login_form')
    LOGIN_USERNAME = (By.ID, 'id_login-username')
    LOGIN_PASSWORD = (By.ID, 'id_login-password')
    LOGIN_SUBMIT = (By.NAME, 'login_submit')

    REGISTRATION_FORM = (By.ID, 'register_form')
    REGISTRATION_EMAIL = (By.ID, 'id_registration-email')
    REGISTRATION_PASSWORD1 = (By.ID, 'id_registration-password1')
    REGISTRATION_PASSWORD2 = (By.ID, 'id_registration-password2')
    REGISTRATION_SUBMIT = (By.NAME, 'registration_submit')

class ProductPageLocators():
    BUTTON_ADD_TO_BASKET = (By.CLASS_NAME, 'btn-add-to-basket')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')    
    MESSAGE_ADD_TO_BASKET = (By.XPATH, "//div[contains(@class,'alert')][1]/div")
    MESSAGE_AMOUNT_BASKET = (By.XPATH, "//div[contains(@class,'alert')][3]//p")
    BASKET_TOTAL = (By.XPATH, "//div[contains(@class,'alert')][3]//strong")