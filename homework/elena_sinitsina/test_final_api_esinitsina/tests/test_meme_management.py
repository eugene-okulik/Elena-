import pytest
import requests


def test_add_meme(create_meme_endpoint, data, meme_user):
    token = meme_user.get_token()
    create_meme_endpoint.create_new_meme(payload=data, token=token)
    create_meme_endpoint.check_that_status_is_200()
    create_meme_endpoint.check_response_info_is_correct(data["info"])


def test_update_meme(update_meme_endpoint, meme_id):
    payload = {
            "id": meme_id,
            "text": "When you saved money and skipped QA",
            "url": "https://mailtrap.io/wp-content/uploads/2020/06/testing_meme4.jpg",
            "tags": ["fun", "QA"],
            "info": {"colors": ["orange", "grey", "white"], "objects": ["picture", "text"]}}
    update_meme_endpoint.update_meme(meme_id, payload)
    update_meme_endpoint.check_that_status_is_200()

    print(f"Response status: {update_meme_endpoint.response.status_code}")
    print(f"Response body: {update_meme_endpoint.response.text}")
    assert update_meme_endpoint.response.status_code == 200
    assert update_meme_endpoint.json.get('text') == payload['text']


def test_delete_meme(delete_meme_endpoint, meme_id):
    delete_meme_endpoint.delete_meme(meme_id)
    delete_meme_endpoint.check_that_status_is_200()
    delete_meme_endpoint.check_if_meme_deleted()
    delete_meme_endpoint.check_status_of_deleted_meme(meme_id)
