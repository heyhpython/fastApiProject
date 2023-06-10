# -*- coding: utf-8 -*-
#
# 模块路由文件
# Author:
# Email:
# Created Time: 2023-06-10
# from typing import Dict
import logging

from fastapi import APIRouter, Body, Depends
from sqlmodel import Session, SQLModel, create_engine, select

from .model import User

# from fastapi import Depends, HTTPException
from .schema import MessageResp  # 通用schema

engine = create_engine("sqlite:///./test.db", echo=True, future=True)
SQLModel.metadata.create_all(engine)
router = APIRouter(
    # dependencies=[Depends(get_token_header)],
    # responses={404: {"description": "Not found"}},
)


def get_db():
    db = Session(engine)
    try:
        yield db
    finally:
        db.close()


@router.get("/", summary="模块测试API", response_model=MessageResp)
async def test_api():
    """模块测试API"""
    return {"message": "ok"}


@router.get("/users", summary="用户列表")
def get_users(db=Depends(get_db)):
    """用户列表"""
    stat = select(User)
    user = db.exec(stat)
    return {"users": user.all()}


@router.post("/users", summary="用户列表")
def create_user(user: User = Body(), db=Depends(get_db)):
    """用户列表"""
    db.add(user)
    logging.error(user.dict())
    db.commit()
    logging.error(user.username)
    return {"data": user.dict()}
