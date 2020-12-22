from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "what is it?" in self.browser.currect_url == "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/", \
            "No login url"

    def should_be_login_form(self):
        self.is_element_present(*LoginPageLocators.FORM_COME_IN), "No login form"
        assert True

    def should_be_register_form(self):
        self.is_element_present(*LoginPageLocators.FORM_REGISTRATION), "No registration form"
        assert True
