import requests
import allure
from test_api_esinitsina.endpoints.endpoint import Endpoint


class PartlyUpdateItem(Endpoint):

    @allure.step('Update an item with partial data')
    def partial_update_item(self, item_id, payload, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.patch(
            f'{self.url}/{item_id}',
            json=payload,
            headers=headers
        )
        self.json = self.response.json()
        return self.response
