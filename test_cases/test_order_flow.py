# -*- coding: utf-8 -*-
"""
Test Case层：下单流程测试用例
"""
import sys
import os

# 手动添加项目根目录到Python路径
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
import allure
from business.order_business import OrderBusiness
from utils.data_loader import load_test_data

@allure.epic("电商平台")
@allure.feature("订单流程")
class TestOrderFlow:
    
    @pytest.fixture(autouse=True)
    def setup(self):
        """测试前置操作"""
        self.order_business = OrderBusiness()
        yield
        # 测试后置清理（可选）
        # 这里可以添加清理测试数据的逻辑
    
    @allure.story("用户成功下单流程")
    @allure.title("正向用例：登录后成功创建订单")
    def test_login_and_create_order_success(self):
        """测试用户登录后能否成功下单"""
        # 准备测试数据
        username = "test_user"
        password = "test123456"
        item_id = 1
        quantity = 2
        
        # 执行业务流程
        order_id = self.order_business.create_order_flow(username, password, item_id, quantity)
        
        # 断言结果
        assert order_id is not None, "订单ID不应为空"
        assert isinstance(order_id, int), "订单ID应为整数"
        allure.attach(f"订单创建成功，订单ID: {order_id}", name="订单信息")
        print(f"✅ 下单成功，订单ID: {order_id}")
    
    @allure.story("数据驱动测试")
    @allure.title("下单功能数据驱动测试 - {case_data[item_id]}")
    @pytest.mark.parametrize("case_data", load_test_data("order_cases"))
    def test_create_order_data_driven(self, case_data):
        """数据驱动测试示例"""
        test_description = f"测试数据: 用户={case_data['username']}, 商品={case_data['item_id']}, 数量={case_data['quantity']}, 预期={case_data['expected']}"
        allure.dynamic.description(test_description)
        
        if case_data["expected"] == "should_success":
            # 预期成功的测试用例
            result = self.order_business.create_order_flow(
                case_data["username"],
                case_data["password"],
                case_data["item_id"],
                case_data["quantity"]
            )
            # 断言订单创建成功
            assert result is not None, "预期下单成功，但订单ID为空"
            assert isinstance(result, int), "订单ID应为整数"
            print(f"✅ 用例通过 - 成功创建订单，订单ID: {result}")
            
        else:
            # 预期失败的测试用例 - 使用pytest.raises捕获异常
            with pytest.raises(Exception) as exc_info:
                self.order_business.create_order_flow(
                    case_data["username"],
                    case_data["password"],
                    case_data["item_id"],
                    case_data["quantity"]
                )
            
            # 验证异常信息中包含预期的错误内容
            error_message = str(exc_info.value)
            assert "失败" in error_message or "错误" in error_message or "不存在" in error_message
            print(f"✅ 用例通过 - 符合预期失败: {error_message}")
