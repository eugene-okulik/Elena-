from pages.eco_friendly_page import EcoFriendly
from conftest import eco_friendly_page

def test_header_title(eco_friendly_page):
    eco_friendly_page.open_page()
    eco_friendly_page.check_page_header_title_is("Eco Friendly")

def test_check_add_cart_button_first_product(eco_friendly_page):
    eco_friendly_page.open_page()
    eco_friendly_page.check_first_product_button()

def test_products_are_displayed(eco_friendly_page):
    eco_friendly_page.open_page()
    eco_friendly_page.check_if_have_products()
