# -*- coding: utf-8 -*-
"""
API Object层：订单接口封装
"""
import requests
from config.config import config

class OrderApi:
    """订单API封装类"""
    
    def create_order(self, session, item_id, quantity=1):
        """
        封装创建订单接口
        :param session: 已认证的session对象
        :param item_id: 商品ID
        :param quantity: 数量
        :return: 响应对象
        """
        url = f"{config.BASE_URL}/api/order"
        data = {
            "item_id": item_id,
            "quantity": quantity
        }
        return session.post(url, json=data, timeout=config.TIMEOUT, verify=config.VERIFY)
