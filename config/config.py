# -*- coding: utf-8 -*-
"""
配置管理层：管理不同环境的配置
"""

class Config:
    """基础配置"""
    BASE_URL = "http://127.0.0.1:8000"  # 您的Flask demo_api地址
    TIMEOUT = 10
    VERIFY = False

# 测试环境配置
class TestConfig(Config):
    DB_HOST = "test-db.example.com"
    DB_NAME = "mall_test"

# 生产环境配置
class ProdConfig(Config):
    BASE_URL = "https://api.yourmall.com"
    DB_HOST = "prod-db.example.com"
    DB_NAME = "mall_prod"

# 默认使用测试环境配置
config = TestConfig()
