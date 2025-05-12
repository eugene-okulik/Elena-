
import pytest
from playwright.sync_api import sync_playwright
from pages.eco_friendly_page import EcoFriendly
from pages.sale_page import Sale


@pytest.fixture()
def eco_friendly_page(page):
    return EcoFriendly(page)

@pytest.fixture()
def sale_page(page):
    return Sale(page)
