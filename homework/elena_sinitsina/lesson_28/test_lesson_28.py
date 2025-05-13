from playwright.sync_api import Page, expect, Request, Route
import json
import time


def test_iphone(page: Page):

    def handle_route(route: Route):
        response = route.fetch()
        body = response.json()

        body['body']['digitalMat'][0]['familyTypes'][0]['productName'] = 'яблокофон 16 про'

        route.fulfill(
            response=response,
            body=json.dumps(body)
        )

    page.route('https://www.apple.com/shop/api/digital-mat?path=library/step0_iphone/digitalmat', handle_route)
    page.goto('https://www.apple.com/shop/buy-iphone')
    page.locator('text=iPhone 16 Pro & >> nth=0').click()
    page.wait_for_selector('div.rf-digitalmat-overlay-content-main', timeout=10000)

    header = page.locator('h2.rf-digitalmat-overlay-header').nth(0)

    expect(header).to_have_text('яблокофон 16 про')
    time.sleep(5)
