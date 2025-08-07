from authentication.user_schema import UserLogoutSchema, UserLoginSchema

from fastapi import APIRouter
from models.user import User
from typing import List


router = APIRouter(
    prefix='/user',
    tags=['user']   
)

