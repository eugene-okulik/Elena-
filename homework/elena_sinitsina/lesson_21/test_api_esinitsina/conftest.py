import pytest
from test_api_esinitsina.endpoints.create_item import CreateItem
from test_api_esinitsina.endpoints.update_item import UpdateItem
from test_api_esinitsina.endpoints.partly_update_item import PartlyUpdateItem
from test_api_esinitsina.endpoints.delete_item import DeleteItem


@pytest.fixture()
def create_item_endpoint():
    return CreateItem()


@pytest.fixture()
def item_id(create_item_endpoint, delete_item_endpoint):
    payload = {
        "name": "TEMP MODEL",
        "data": {
            "generation": "1st",
            "capacity GB": 1000
        }
    }
    create_item_endpoint.new_item(payload)

    yield create_item_endpoint.item_id
    delete_item_endpoint.delete_item(create_item_endpoint.item_id)
    delete_item_endpoint.check_status_of_deleted_item(create_item_endpoint.item_id)


@pytest.fixture()
def update_item_endpoint():
    return UpdateItem()


@pytest.fixture()
def partly_update_item_endpoint():
    return PartlyUpdateItem()


@pytest.fixture()
def delete_item_endpoint():
    return DeleteItem()
