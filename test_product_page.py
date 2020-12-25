import pytest
from pages.product_page import ProductPage
import time
from pages.login_page import LoginPage


product_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
urls = [f"{product_link}/?promo=offer{no}" for no in range(10)]
urls[7] = pytest.param("7", marks=pytest.mark.xfail)


# @pytest.mark.parametrize('link', urls)
# def test_guest_can_add_product_to_basket(browser, link):
#     cart = ProductPage(browser, link)
#     cart.open()
#     cart.add_to_cart()
#     cart.solve_quiz_and_get_code()
#     cart.price_correct()
#     cart.items_correct()
def test_guest_cant_see_success_message_after_adding_product_to_cart(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    cart = ProductPage(browser, link)
    cart.open()
    cart.add_to_cart()
    cart.should_not_be_success_message()


def test_user_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    cart = ProductPage(browser, link)
    cart.open()
    cart.should_not_be_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.login_link
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    login = LoginPage(browser, link)
    login.open()
    login.go_to_login_page()
    login.should_be_login_page()


def test_message_disappeared_after_adding_product_to_cart(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/hacking-exposed-wireless_208/"
    cart = ProductPage(browser, link)
    cart.open()
    cart.add_to_cart()
    cart.success_message_is_disappeared()
