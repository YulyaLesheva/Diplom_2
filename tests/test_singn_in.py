import pytest
import requests

from data.test_data import generate_email, generate_password, generate_name
from data.urls import REGISTER_URL


class TestSignIn:
    def test_register_unique_user(self, unique_user):
        res = requests.post(REGISTER_URL, json=unique_user)
        assert res.status_code == 200
        assert res.json()["success"] is True

    def test_register_existing_user(self, registered_user):
        res = requests.post(REGISTER_URL, json=registered_user)
        assert res.status_code == 403
        assert res.json()["message"] == "User already exists"

    @pytest.mark.parametrize("missing_field", ["email", "password", "name"])
    def test_register_missing_field(self, missing_field):

        user = {
            "email": generate_email(),
            "password": generate_password(),
            "name": generate_name()
        }

        user.pop(missing_field)
        res = requests.post(REGISTER_URL, json=user)
        assert res.status_code == 403
        assert res.json()["message"] == "Email, password and name are required fields"
