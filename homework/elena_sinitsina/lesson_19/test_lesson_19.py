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
def new_post_id():
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
    post_id = response.json()['id']
    print(post_id)
    yield post_id
    print('deleting the post')
    requests.delete(f'https://api.restful-api.dev/objects/{post_id}')


@pytest.mark.critical
def test_get_one_post(new_post_id):
    response = requests.get(f'https://api.restful-api.dev/objects/{new_post_id}').json()
    assert response['id'] == new_post_id


@pytest.mark.critical
@pytest.mark.parametrize('body', [
    {"name": "NEW MODEL 1", "data": {"generation": "11th", "capacity GB": 1000}},
    {"name": "NEW MODEL 2", "data": {"generation": "12th", "capacity GB": 2000}},
    {"name": "NEW MODEL 3", "data": {"generation": "13th", "capacity GB": 3000}}
])
def test_add_post(body):
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


@pytest.mark.regression
def test_one():
    assert 1 == 1


@pytest.mark.parametrize('logins', [random.randint(1, 3) for _ in range(3)])
def test_two(logins):
    print(logins)
    assert 1 == 1


def test_three():
    assert 1 == 1


