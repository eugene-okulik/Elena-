import pytest
import requests


TEST_DATA = [
    {"name": "MODEL 100","data": {"generation": "104th","capacity GB": 5000}}, 
    {"name": "MODEL 200","data": {"generation": "200th","capacity GB": 6000}}
]

NEGATIVE_DATA = [
    {"name": ["MODEL 100"], "data": {"generation": "104th", "capacity GB": 5000}},
    {"name": {"MODEL 200": ""}, "data": {"generation": "200th", "capacity GB": 6000}}
]


@pytest.mark.parametrize('data', TEST_DATA)
def test_add_item(create_item_endpoint, data):
    create_item_endpoint.new_item(payload=data)
    create_item_endpoint.check_that_status_is_200()
    create_item_endpoint.check_response_title_is_correct(data["name"])


@pytest.mark.parametrize('data', NEGATIVE_DATA)
def test_item_with_negative_data(create_item_endpoint, data):
    create_item_endpoint.new_item(data, expect_failure=True)
    create_item_endpoint.check_bad_request()


def test_put_item(update_item_endpoint, item_id):
    payload = {
        "name": "UPDATED MODEL 2024",
        "data": {
            "generation": "15th",
            "capacity GB": 5000
        }
    }
    update_item_endpoint.make_changes_in_item(item_id, payload)
    update_item_endpoint.check_that_status_is_200()
    update_item_endpoint.check_response_title_is_correct(payload["name"])


def test_patch_item(partly_update_item_endpoint, item_id):
    payload = {
        "name": "SuperUpdate MODEL UPD",
        "data": {
            "generation": "12th"
        }
    }
    partly_update_item_endpoint.partial_update_item(item_id, payload)
    partly_update_item_endpoint.check_that_status_is_200()
    partly_update_item_endpoint.check_response_title_is_correct(payload["name"])


def test_delete_item(delete_item_endpoint, item_id):
    delete_item_endpoint.delete_item(item_id)
    delete_item_endpoint.check_that_status_is_200()
    delete_item_endpoint.check_if_item_deleted()
