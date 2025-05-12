from conftest import sale_page


def test_header_title(sale_page):
    sale_page.open_page()
    sale_page.check_page_header_title_is("Sale")


def test_mens_bargains_navigation(sale_page):
    sale_page.open_page()
    sale_page.click_mens_bargains()


def test_get_products_count(sale_page):
    sale_page.open_page()
    sale_page.get_products_count()
