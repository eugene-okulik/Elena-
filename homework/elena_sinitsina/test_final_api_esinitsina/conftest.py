import pytest
from test_final_api_esinitsina.endpoints.create_meme import CreateMeme
from test_final_api_esinitsina.endpoints.endpoint import MemeUser
from test_final_api_esinitsina.endpoints.update_meme import UpdateMeme
from test_final_api_esinitsina.endpoints.delete_meme import DeleteMeme


@pytest.fixture()
def create_meme_endpoint():
    return CreateMeme()


@pytest.fixture()
def meme_user():
    user = MemeUser()
    user.on_start()
    return user


@pytest.fixture()
def data():
    return {
        "text": "Devs skipped QA",
        "url": "https://mailtrap.io/wp-content/uploads/2020/06/testing_meme4.jpg",
        "tags": ["fun", "QA"], "info": {"colors": ["orange", "grey", "white"], "objects": ["picture", "text"]}
         }


@pytest.fixture()
def update_meme_endpoint():
    return UpdateMeme()


@pytest.fixture()
def meme_id(create_meme_endpoint, data, meme_user, delete_meme_endpoint):
    token = meme_user.get_token()
    print(f"Token: {token}")
    print(f"Payload: {data}")
    response = create_meme_endpoint.create_new_meme(payload=data, token=token)
    print(f"Create meme response: {response}")

    create_meme_endpoint.create_new_meme(data)

    yield create_meme_endpoint.meme_id
    delete_meme_endpoint.delete_meme(create_meme_endpoint.meme_id)
    delete_meme_endpoint.check_status_of_deleted_meme(create_meme_endpoint.meme_id)


@pytest.fixture()
def delete_meme_endpoint():
    return DeleteMeme()
