# -*- coding: utf-8 -*-
"""
请求工具类
"""
import requests

def safe_request(method, url, **kwargs):
    """安全的请求封装"""
    try:
        response = requests.request(method, url, **kwargs)
        response.raise_for_status()  # 如果状态码不是200，抛出异常
        return response
    except requests.exceptions.RequestException as e:
        raise Exception(f"请求失败: {str(e)}")
