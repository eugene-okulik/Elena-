import allure


class Endpoint:
    url = 'https://api.restful-api.dev/objects'
    response = None
    json = None
    headers = {'Content-Type': 'application/json'}

    @allure.step('Check that title is the same as sent')
    def check_response_title_is_correct(self, name):
        assert self.response is not None, "Response is None!"
        assert self.json is not None, "JSON response is None!"
        assert self.json.get('name') == name, 'name is not name'

    @allure.step('Check if response is 200')
    def check_that_status_is_200(self):
        print(f"Response status: {self.response.status_code}")
        print(f"Response body: {self.response.text}")
        assert self.response.status_code == 200, 'status is not 200'

    @allure.step('Check that error 400 returned')
    def check_bad_request(self):
        assert self.response.status_code == 400, 'status is not 400'

    @allure.step('Check if the item was deleted')
    def check_if_item_deleted(self):
        print(f"Response status: {self.response.status_code}")
        print(f"Response body: {self.response.text}")
        assert self.response.status_code in [200, 204], 'status is not 200 or 204'
