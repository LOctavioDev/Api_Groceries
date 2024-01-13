from fastapi import APIRouter
from ..config.db import conn
from ..schemas.user import userEntity, usersEntity
from ..models.user import User

user = APIRouter()

@user.get('/users')
def find_all_users():
    return usersEntity(conn.local.user.find()) 

@user.post('/users')
def create_user(user: User):
    new_user = dict(user)
    print(new_user)
    return "recived"

@user.get('/users/{id}')
def find_users():
    return 'hello world'

@user.put('/user/{id}')
def update_user():
    return 'hello world'

@user.delete('/user/{id}')
def delete_user():
    return 'hello world'
