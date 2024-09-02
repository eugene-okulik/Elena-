import random

import requests
import pytest


@pytest.fixture(scope='session', autouse=True)
def start_and_end_testing():
    print("Start testing")
    yield
    print("Testing completed")


@pytest.fixture(autouse=True)
def before_after_test():
    print("before test")
    yield
    print("after test")


@pytest.fixture()
def new_item_id():
    body = {
        "name": "NEW MODEL",
        "data": {
            "generation": "11rd",
            "capacity GB": 1000
        }
    }
    headers = {"content-type": "application/json"}
    response = requests.post(
        'https://api.restful-api.dev/objects',
        json=body,
        headers=headers
    )
    item_id = response.json()['id']
    print(item_id)
    yield item_id
    print('deleting the item')
    requests.delete(f'https://api.restful-api.dev/objects/{item_id}')


@pytest.mark.critical
def test_get_one_item(new_item_id):
    response = requests.get(f'https://api.restful-api.dev/objects/{new_item_id}').json()
    assert response['id'] == new_item_id


@pytest.mark.critical
@pytest.mark.parametrize('body', [
    {"name": "NEW MODEL 1", "data": {"generation": "11th", "capacity GB": 1000}},
    {"name": "NEW MODEL 2", "data": {"generation": "12th", "capacity GB": 2000}},
    {"name": "NEW MODEL 3", "data": {"generation": "13th", "capacity GB": 3000}}
])
def test_add_item(body):
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        'https://api.restful-api.dev/objects',
        json=body,
        headers=headers
    )
    print(response.status_code)
    print(response.text)
    assert response.status_code == 200
    assert isinstance(response.json()['id'], str)


@pytest.mark.medium
def test_patch_item(new_item_id):
    patch_body = {
        "name": "SUPERNEW MODEL UPD",
        "data": {
            "generation": "12th",
            "capacity GB": 3000
        }
    }
    headers = {"content-type": "application/json"}
    response = requests.patch(
        f'https://api.restful-api.dev/objects/{new_item_id}',
        json=patch_body,
        headers=headers
    )
    assert response.status_code == 200
    updated_post = response.json()
    assert updated_post['name'] == "SUPERNEW MODEL UPD"
    assert updated_post['data']['generation'] == "12th"
    assert updated_post['data']['capacity GB'] == 3000


@pytest.mark.regression
def test_delete_post(new_item_id):
    delete_response = requests.delete(f'https://api.restful-api.dev/objects/{new_item_id}')
    assert delete_response.status_code == 200
    get_response = requests.get(f'https://api.restful-api.dev/objects/{new_item_id}')
    assert get_response.status_code == 404


@pytest.mark.regression
def test_one():
    assert 1 == 1


@pytest.mark.parametrize('logins', [random.randint(1, 3) for _ in range(3)])
def test_two(logins):
    print(logins)
    assert 1 == 1


def test_three():
    assert 1 == 1








