import requests
import allure
from test_api_esinitsina.endpoints.endpoint import Endpoint


class DeleteItem(Endpoint):

    @allure.step('Delete an item')
    def delete_item(self, item_id, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.delete(
            f'{self.url}/{item_id}',
            headers=headers
        )
        self.json = self.response.json()
        return self.response
