# utils/data_loader.py
def load_test_data(data_type):
    """
    加载测试数据
    :param data_type: 数据类型，如 'order_cases'
    :return: 测试数据列表
    """
    test_data = {
        'order_cases': [
            {
                'username': 'test_user',
                'password': 'test123456', 
                'item_id': 1,           # 存在的商品 → 预期成功
                'quantity': 2,
                'expected': 'should_success'
            },
            {
                'username': 'test_user',
                'password': 'test123456',
                'item_id': 9990,         # 不存在的商品 → 预期失败
                'quantity': 1,
                'expected': 'should_fail'
            },
            {
                'username': 'test_user',
                'password': 'test123456',
                'item_id': 1,           # 存在的商品，但数量太大 → 预期失败
                'quantity': 1000,       # 超过库存数量
                'expected': 'should_fail'
            }
        ]
    }
    
    return test_data.get(data_type, [])
