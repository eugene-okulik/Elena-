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

    @allure.step('Check if the item was deleted')
    def check_if_item_deleted(self):
        print(f"Response status: {self.response.status_code}")
        print(f"Response body: {self.response.text}")
        assert self.response.status_code in [200, 204], 'status is not 200, 204'

    def check_status_of_deleted_item(self, item_id):
        headers = self.headers
        self.response = requests.get(
            f'{self.url}/{item_id}',
            headers=headers
        )
        self.json = self.response.json()
        print(f"Response status of follow-up GET request: {self.response.status_code}")
        print(f"Response body of follow-up GET request: {self.response.text}")
        assert self.response.status_code == 404, 'Item still exists after deletion'
