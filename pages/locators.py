from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    FORM_COME_IN = (By.ID, "login_form")
    FORM_REGISTRATION = (By.ID, "register_form")
