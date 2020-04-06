from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not present"
        assert self.is_element_present(*LoginPageLocators.LOGIN_USERNAME), "Username for login form is not present"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD), "Password for login form is not present"
        assert self.is_element_present(*LoginPageLocators.LOGIN_SUBMIT), "Submit button for login form is not present"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Registration form is not present"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_EMAIL), "Email for registration form is not present"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD1), "Password1 for registration form is not present"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD2), "Password2 for registration form is not present"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_SUBMIT), "Submit button for registration form is not present"