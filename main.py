from fastapi import FastAPI
from pydantic import BaseModel
from database import *
from User import User

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/users/")
async def get_all_users():
    query = "select * from users"
    return execute_query(query)

@app.get("/users/{id}")
async def get_user(id: int):
    query = f"select * from users where id = {id}"
    return execute_query(query)

@app.post("/user/")
async def create_user(user: User):
    query = f"insert into users (username, password) values ('{user.username}', '{user.password}')"
    return execute_query(query)

@app.delete("/user/{id}")
async def delete_user(id: int):
    query = f"delete from users where id = {id}"
    return execute_query(query)


