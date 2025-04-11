from time import sleep
from playwright.sync_api import expect


def test_alert_confirm(page):
    page.goto('https://www.qa-practice.com/elements/alert/confirm')
    page.wait_for_selector('a.a-button')

    def handle_dialog(dialog):
        dialog.accept()
    page.on("dialog", handle_dialog)
    button = page.query_selector('a.a-button')
    button.click(force=True)
    result_text = page.locator('#result-text')
    expect(result_text).to_have_text('Ok')


def test_new_page(page):
    page.goto('https://www.qa-practice.com/elements/new_tab/button')
    button = page.query_selector('a#new-page-button.a-button')
    button.click()
    new_tab = page.context.wait_for_event("page")
    new_tab.wait_for_selector('p#result-text', state='visible', timeout=60000)
    result_text = new_tab.locator('p#result-text')
    expect(result_text).to_have_text('I am a new page in a new tab')
    original_button = page.locator('a#new-page-button.a-button')
    expect(original_button).to_be_enabled()


def test_click_color(page):
    page.goto('https://demoqa.com/dynamic-properties')
    page.wait_for_selector('button#colorChange', state='visible')
    button = page.locator('button#colorChange')
    expect(button).to_have_css('color', 'rgb(220, 53, 69)')
    button.click()
