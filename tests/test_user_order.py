import requests

from data.urls import USER_ORDERS_URL


class TestUserOrders:
    def test_get_user_orders_with_auth(self, authorized_headers):
        res = requests.get(USER_ORDERS_URL, headers=authorized_headers)
        assert res.status_code == 200
        assert res.json()["success"] is True

    def test_get_user_orders_without_auth(self):
        res = requests.get(USER_ORDERS_URL)
        assert res.status_code == 401
        assert res.json()["message"] == "You should be authorised"
