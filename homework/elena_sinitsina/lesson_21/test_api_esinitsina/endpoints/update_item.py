import requests
import allure
from test_api_esinitsina.endpoints.endpoint import Endpoint


class UpdateItem(Endpoint):

    @allure.step('Update an item')
    def make_changes_in_item(self, item_id, payload, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.put(
        f'{self.url}/{item_id}',
            json=payload,
            headers=headers
        )
        self.json = self.response.json()
        return self.response
