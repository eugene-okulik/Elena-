import requests
import allure
from test_api_esinitsina.endpoints.endpoint import Endpoint


class CreateItem(Endpoint):
    item_id = None

    @allure.step('Create a new item')
    def new_item(self, payload, headers=None, expect_failure=False):
        headers = headers if headers else self.headers
        self.response = requests.post(
            self.url,
            json=payload,
            headers=headers
        )
        if self.response.status_code == 200 and "application/json" in self.response.headers.get('Content-Type', ''):
            self.json = self.response.json()
            if 'id' in self.json:
                self.item_id = self.json['id']
            else:
                raise KeyError("Response JSON does not contain 'id'")
        elif not expect_failure:
            self.response.raise_for_status()

