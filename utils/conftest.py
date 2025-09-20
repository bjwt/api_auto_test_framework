# -*- coding: utf-8 -*-
"""
Pytest配置文件：定义全局fixture
"""
import pytest
from business.order_business import OrderBusiness

@pytest.fixture(scope="session")
def auth_session():
    """全局共享的已认证session"""
    business = OrderBusiness()
    session = business.login_and_get_session("test_user", "test123456")
    yield session
    session.close()
