from playwright.sync_api import Page, Locator


class BasePage:
    base_url = 'https://magento.softwaretestingboard.com/'
    page_url = None

    def __init__(self, page: Page):
        self.page = page

    def open_page(self):
        if self.page_url:
            self.page.goto(f'{self.base_url}{self.page_url}')
        else:
            raise NotImplementedError('Page cannot be opened for this class')

    def find(self, locator):
        return self.page.locator(locator)
