# -*- coding: utf-8 -*-
"""
Business Layer层：下单业务流程封装
"""
from api.login_api import LoginApi
from api.order_api import OrderApi
import requests

class OrderBusiness:
    """订单业务类"""
    
    def login_and_get_session(self, username, password):
        """
        业务逻辑：登录并获取已认证的session
        :return: 携带token的session对象
        """
        # 调用API Object层
        login_api = LoginApi()
        response = login_api.login(username, password)
        
        if response.status_code != 200:
            raise Exception(f"登录失败: {response.text}")
        
        # 提取token
        token = response.json().get('token')
        if not token:
            raise Exception("登录响应中未找到token")
        
        # 创建session并设置token
        session = requests.Session()
        session.headers.update({
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        })
        
        return session
    
    def create_order_flow(self, username, password, item_id, quantity=1):
        """
        完整的下单业务流程：登录 -> 创建订单
        :return: 订单ID
        """
        # 1. 登录获取session
        session = self.login_and_get_session(username, password)
        
        # 2. 创建订单
        order_api = OrderApi()
        response = order_api.create_order(session, item_id, quantity)
        
        if response.status_code != 200:
            raise Exception(f"下单失败: {response.text}")
        
        order_data = response.json()
        return order_data.get('data', {}).get('order_id')
