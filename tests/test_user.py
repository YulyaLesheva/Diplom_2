import uuid

import requests

from data.urls import USER_URL


class TestUserUpdate:
    def test_update_user_with_auth(self, authorized_headers):
        data = {"name": "Updated User", "email": f"upd_{uuid.uuid4()}@ya.ru"}
        res = requests.patch(USER_URL, json=data, headers=authorized_headers)
        assert res.status_code == 200
        assert res.json()["user"]["name"] == data["name"]

    def test_update_user_without_auth(self):
        res = requests.patch(USER_URL, json={"name": "New Name"})
        assert res.status_code == 401
        assert res.json()["message"] == "You should be authorised"
