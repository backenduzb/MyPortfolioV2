from fastapi import APIRouter, Depends, HTTPException

router = APIRouter(
    prefix='/chat',
    tags=['chat']
)