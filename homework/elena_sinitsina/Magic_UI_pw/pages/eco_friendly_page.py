from pages.base_page import BasePage


class EcoFriendly(BasePage):
    page_url = "collections/eco-friendly.html"


    def check_page_header_title_is(self, text):
        header_title = self.page.locator("h1")
        header_text = header_title.inner_text()
        assert header_text == text, f"Expected header '{text}', but got '{header_text}'"

    def check_first_product_button(self):
        first_product_button = self.page.locator(".products-grid .product-item:first-child button.tocart")
        assert first_product_button.is_visible(), "Button 'Add to Cart' is missing at the first product"

    def check_if_have_products(self):
        products = self.page.locator(".products-grid .product-item")
        assert products.count() > 0, "Products are not displayed on this page"
