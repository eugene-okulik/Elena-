import requests
import json


def all_posts():
    response = requests.get('https://api.restful-api.dev/objects')
    json_data = response.json()
#   print(json.dumps(json_data, indent=4))


all_posts()


def post_a_post():
    body = {
        "name": "Huawei NEW",
        "data": {
            "generation": "10rd",
            "capacity GB": 600
        }
    }
    headers = {"content-type": "application/json"}
    response = requests.post(
        'https://api.restful-api.dev/objects',
        json=body,
        headers=headers
    )
    print(f"Actual Status Code: {response.status_code}")
    print(f"Response Content: {response.text}")
    response_json = response.json()
    print(f"Response JSON: {json.dumps(response_json, indent=4)}")

    assert response.status_code == 200, f'Status code is incorrect, got {response.status_code}'
    assert 'id' in response_json, 'Id is missing in the response'
    return response_json['id']


post_a_post()


def new_post():
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
    return response.json()['id']


def put_a_post(post_id):
    body = {
        "name": "NEW MODEL UPD",
        "data": {
            "generation": "11rd",
            "capacity GB": 1000
        }
    }
    headers = {"content-type": "application/json"}
    response = requests.put(
        f'https://api.restful-api.dev/objects/{post_id}',
        json=body,
        headers=headers
    )
    print(f"Actual Status Code: {response.status_code}")

    print(f"Response Content: {response.text}")

    response_json = response.json()
    print(f"Response JSON: {json.dumps(response_json, indent=4)}")

    assert response_json.get('name') == 'NEW MODEL UPD', 'Name was not updated correctly'


post_id = post_a_post()
put_a_post(post_id)


def patch_a_post(post_id):
    body = {
        "name": "SUPERNEW MODEL UPD"
    }
    headers = {"content-type": "application/json"}
    response = requests.patch(
        f'https://api.restful-api.dev/objects/{post_id}',
        json=body,
        headers=headers
    )
    print(f"Actual Status Code: {response.status_code}")

    print(f"Response Content: {response.text}")

    response_json = response.json()
    print(f"Response JSON: {json.dumps(response_json, indent=4)}")

    assert response_json.get('name') == 'SUPERNEW MODEL UPD', 'Name was not updated correctly'


patch_a_post(post_id)


def delete_a_post(post_id):
    response = requests.delete(
        f'https://api.restful-api.dev/objects/{post_id}')
    print(f"Actual Status Code: {response.status_code}")

    print(f"Response Content: {response.text}")

    response_json = response.json()
    print(f"Response JSON: {json.dumps(response_json, indent=4)}")


delete_a_post(post_id)

