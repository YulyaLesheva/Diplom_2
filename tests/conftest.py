import pytest
import requests

from data import urls
from data.test_data import generate_email, generate_password, generate_name


@pytest.fixture
def unique_user():
    return {
        "email": generate_email(),
        "password": generate_password(),
        "name": generate_name()
    }


@pytest.fixture
def registered_user(unique_user):
    requests.post(urls.REGISTER_URL, json=unique_user)
    return unique_user


@pytest.fixture
def access_token(registered_user):
    res = requests.post(urls.LOGIN_URL, json=registered_user)
    token = res.json()["accessToken"].split()[1]
    yield token
    requests.delete(urls.USER_URL, headers={"Authorization": f"Bearer {token}"})


@pytest.fixture
def authorized_headers(access_token):
    return {"Authorization": f"Bearer {access_token}"}
