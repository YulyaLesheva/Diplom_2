import requests

from data.urls import BASE_URL, ORDER_URL


class TestOrderCreation:
    def test_create_order_with_auth(self, authorized_headers):
        ingredients = requests.get(f"{BASE_URL}/api/ingredients").json()["data"]
        ingredient_ids = [i["_id"] for i in ingredients]
        res = requests.post(ORDER_URL, json={"ingredients": ingredient_ids}, headers=authorized_headers)
        assert res.status_code == 200
        assert res.json()["success"] is True

    def test_create_order_without_auth(self):
        ingredients = requests.get(f"{BASE_URL}/api/ingredients").json()["data"]
        ingredient_ids = [i["_id"] for i in ingredients]
        res = requests.post(ORDER_URL, json={"ingredients": ingredient_ids})
        assert res.status_code == 200
        assert res.json()["success"] is True

    def test_create_order_without_ingredients(self, authorized_headers):
        res = requests.post(ORDER_URL, json={"ingredients": []}, headers=authorized_headers)
        assert res.status_code == 400
        assert res.json()["message"] == "Ingredient ids must be provided"

    def test_create_order_with_invalid_ingredients(self, authorized_headers):
        res = requests.post(ORDER_URL, json={"ingredients": ["invalid_hash"]}, headers=authorized_headers)
        assert res.status_code == 400
