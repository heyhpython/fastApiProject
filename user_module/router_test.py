# -*- coding: utf-8 -*-
#
# 接口单元测试脚本（使用pytest）
#     sudo docker exec -ti container_name pytest user_module/router_test.py
#
# Author:
# Email:
# Created Time: 2023-06-10
import os
import sys

run_path = os.path.dirname(os.path.dirname(__file__))
sys.path.insert(0, run_path)
print("运行目录:", run_path)


def test_api():
    """单元测试代码"""
    assert 1 == 1
