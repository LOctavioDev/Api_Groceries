from fastapi import APIRouter, Response, status
from ..config.db import conn
from ..schemas.user import userEntity, usersEntity
from ..models.user import User
from passlib.hash import sha256_crypt
from pydantic import BaseModel
from bson import ObjectId
from starlette.status import HTTP_204_NO_CONTENT

user = APIRouter()

db_extrema = [
    {
        "id": 1,
        "nombre": "Octavio",
        "apellido": "Lopez"
    }
    ,
    {
        "id": 2,
        "nombre": "Briones",
        "apellido": "Hernandez"
    }
]

@user.post("/insertOne")
def insertOne(user: dict):
    db_extrema.append(user)
    
    return db_extrema


@user.get("/getOne/{id}")
def getOne(id: int):
    for persona in db_extrema:
        if persona["id"] == id:
            return persona
    return None


@user.get("/getAll")
def getAll():
    return db_extrema


@user.delete("/deleteOne/{id}")
def deleteOne(id: int):
    global db_extrema
    for i, persona in enumerate(db_extrema):
        if persona["id"] == id:
            del db_extrema[i]
            return db_extrema
    return "Elemento no encotrado"
    

class PersonaUpdate(BaseModel):
    nombre: str
    apellido: str
    

@user.put("/updateOne/{id}")
def updateOne(id: int, persona_update: PersonaUpdate):
    global db_extrema
    for persona in db_extrema:
        if persona["id"] == id:
            persona["nombre"] = persona_update.nombre
            persona["apellido"] = persona_update.apellido
            return db_extrema
    return "usuario no encontrado"
            
    



"""-----------------------------------"""

#GET ALL USERS 
@user.get("/users", response_model=list[User])
def find_all_users():
    return usersEntity(conn.groceriesdb.user.find()) 


#ADD A USER WITH ENCRIPTATION
@user.post("/users")
def create_user(user: User):
    new_user = dict(user)
    new_user["password"] = sha256_crypt.encrypt(new_user["password"])
    del new_user["id"]
    
    id = conn.groceriesdb.user.insert_one(new_user).inserted_id
    user = conn.groceriesdb.user.find_one({"_id": id})

    return userEntity(user)


#GET USER BY ID
@user.get("/user/{id}")
def find_user(id: str):
    return userEntity(conn.groceriesdb.user.find_one({"_id": ObjectId(id)}))


#UPDATE A USER 
@user.put('/user/{id}')
def update_user(id: str, user: User):
    conn.groceriesdb.user.find_one_and_update(
            {
                "_id": ObjectId(id)
            },
            {   
                 "$set": dict(user)
            }
            )
    return userEntity(conn.groceriesdb.user.find_one({"_id": ObjectId(id)} ))



#DELETE A USER BY ID
@user.delete('/user/{id}')
def delete_user(id: str):
    userEntity(conn.groceriesdb.user.find_one_and_delete({"_id": ObjectId(id)}))   
    return Response(status_code=HTTP_204_NO_CONTENT)

