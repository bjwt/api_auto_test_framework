# -*- coding: utf-8 -*-
"""
API Object层：登录接口封装
"""
import requests
from config.config import config

class LoginApi:
    """登录API封装类"""
    
    def login(self, username, password):
        """
        封装登录接口
        :param username: 用户名
        :param password: 密码
        :return: 响应对象
        """
        url = f"{config.BASE_URL}/api/login"
        data = {
            "username": username,
            "password": password
        }
        
        # 这里直接返回响应对象，不处理业务逻辑
        return requests.post(url, json=data, timeout=config.TIMEOUT, verify=config.VERIFY)
