# -*- coding: utf-8 -*-
import requests

# 测试登录
login_url = "http://127.0.0.1:8000/api/login"
data = {"username": "test_user", "password": "test123456"}
response = requests.post(login_url, json=data)
print("登录响应:", response.json())
token = response.json()['token']

# 测试下单（使用登录获取的token）
order_url = "http://127.0.0.1:8000/api/order"
headers = {"Authorization": f"Bearer {token}"}
order_data = {"item_id": 1, "quantity": 2}
response = requests.post(order_url, json=order_data, headers=headers)
print("下单响应:", response.json())
