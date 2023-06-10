# -*- coding: utf-8 -*-
#
# 模块路由配置文件
# Author:
# Email:
# Created Time: 2023-06-10
from pydantic import BaseModel, Field


class MessageResp(BaseModel):
    """通用返回消息"""

    message: str = Field(..., description="返回消息")
    code: int = Field(0, description="返回码")
    data: dict = Field({}, description="返回数据")
    error: str = Field("", description="错误信息")
    extra: dict = Field({}, description="额外信息")
