from utils import project_ec
from pages.base_page import BasePage
from playwright.sync_api import expect


class Sale(BasePage):
    page_url = "sale.html"

    def check_page_header_title_is(self, text):
        header_title = self.find("h1")
        header_text = header_title.inner_text()
        assert header_text == text, f"Expected header '{text}', but got '{header_title.text}'"

    def click_mens_bargains(self):
        mens_bargains = self.page.locator(
            '//a[@href="https://magento.softwaretestingboard.com/promotions/men-sale.html"]'
            '//strong[contains(text(), "Men’s Bargains")]'
        )
        mens_bargains.wait_for(state="visible")
        mens_bargains.click()
        assert "men-sale.html" in self.page.url, "Navigation to Men's Bargains failed"

    def get_products_count(self):
        mens_jackets = self.page.locator('a[href*="jackets-men.html"]:has-text("Jackets")').nth(1)
        mens_jackets.wait_for(state="visible")
        mens_jackets.click()
        self.page.wait_for_load_state("load")
        products = self.page.locator(".product-item")
        products_count = products.count()
        assert products_count > 0, "No products found on Sale page"
        return products_count
