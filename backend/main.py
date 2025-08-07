from fastapi import FastAPI
from authentication import authentication
from routers import (
    user_routers,
)
from models.user import User
from tortoise.contrib.fastapi import register_tortoise
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(authentication.router)
app.include_router(user_routers.router)
register_tortoise(
    app,
    db_url='sqlite://db.sqlite3',
    modules={'models':["models.user"]},
    generate_schemas=True,
    add_exception_handlers=True
)