import allure
import requests


class Endpoint:
    url = 'http://167.172.172.115:52355'
    response = None
    json = None
    headers = {'Content-Type': 'application/json'}

    @allure.step('Check that info is the same as sent')
    def check_response_info_is_correct(self, info):
        assert self.response is not None, "Response is None!"
        assert self.json is not None, "JSON response is None!"
        assert self.json.get('info') == info, 'info does not match the expected info'

    @allure.step('Check if response is 200')
    def check_that_status_is_200(self):
        print(f"Response status: {self.response.status_code}")
        print(f"Response body: {self.response.text}")
        assert self.response.status_code == 200, 'status is not 200'


class MemeUser:
    token = None

    def on_start(self):
        response = requests.post(
            'http://167.172.172.115:52355/authorize',
            json={'name': 'Bublik'}
        )
        assert response.status_code == 200, "Authorization request failed"

        response_json = response.json()
        print(f"Response JSON: {response_json}")

        self.token = response_json.get('token')
        print(f"Token: {self.token}")
        assert self.token, "Failed to retrieve token"

    def get_token(self):
        if not self.token:
            self.on_start()
        print(f"Token: {self.token}")
        return self.token
