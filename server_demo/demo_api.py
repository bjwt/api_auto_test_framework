# -*- coding: utf-8 -*-
from flask import Flask, request, Response
import json

app = Flask(__name__)

# 订单ID计数器
order_counter = 10000

def json_response(data: dict, status: int = 200, pretty: bool = True):
    """
    通用 JSON 响应函数
    :param data: 要返回的字典
    :param status: HTTP 状态码
    :param pretty: 是否格式化输出（开发环境建议 True，线上建议 False）
    """
    if pretty:
        body = json.dumps(data, ensure_ascii=False, indent=2) + "\n" # 带缩进和换行
    else:
        body = json.dumps(data, ensure_ascii=False, separators=(",", ":")) + "\n"  # 紧凑格式

    return Response(body, status=status, mimetype="application/json")

def generate_order_id():
    """生成递增订单ID"""
    global order_counter
    order_id = order_counter
    order_counter += 1
    return order_id

# 模拟用户数据库
fake_users_db = {"test_user": {"password": "test123456", "token": "fake_token_123"}}
fake_items_db = {
    1: {"name": "测试商品1", "price": 99.9, "stock": 100},
    2: {"name": "测试商品2", "price": 199.9, "stock": 50},
    888: {"name": "测试商品888", "price": 999.9, "stock": 10}
}

@app.route('/api/login', methods=['POST'])
def login():
    login_data = request.get_json()
    username = login_data.get('username')
    password = login_data.get('password')

    user = fake_users_db.get(username)
    if not user or user["password"] != password:
        return json_response({"code": 401, "msg": "用户名或密码错误"}, 401)

    return json_response({"code": 200, "msg": "登录成功", "token": user["token"]})

@app.route('/api/order', methods=['POST'])
def create_order():
    auth_header = request.headers.get('Authorization')
    if not auth_header or auth_header != 'Bearer fake_token_123':
        return json_response({"code": 401, "msg": "无效的Token"}, 401)

    order_data = request.get_json()
    item_id = order_data.get('item_id')
    quantity = order_data.get('quantity', 1)

    item = fake_items_db.get(item_id)
    if not item:
        return json_response({"code": 404, "msg": "商品不存在"}, 404)

    if item["stock"] < quantity:
        return json_response({"code": 400, "msg": "库存不足"}, 400)

    # 扣减库存
    item["stock"] -= quantity
    order_id = generate_order_id()

    return json_response({
        "code": 200,
        "msg": "下单成功",
        "data": {
            "order_id": order_id,
            "item_name": item["name"],
            "total_price": item["price"] * quantity
        }
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
