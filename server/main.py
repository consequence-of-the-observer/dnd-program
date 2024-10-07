from fastapi import FastAPI 
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

import sqlite3
import uuid

class User(BaseModel):
    fname: str
    lname: str
    username: str
    password: str
    email: str
    userType: str

class Con_User(BaseModel):
    username: str
    password: str

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

def sql_createUser(data):
    conn = sqlite3.connect('server.db')

    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS users
                    (first_name, last_name, username, password, email, uuid, userType)''')
    cursor.execute("INSERT INTO users VALUES ('"+data['first_name']+"','"+data['last_name']+"','"+data['username']+"','"+data['password']+"','"+data['email']+"','"+data['uuid']+"', '"+data['userType']+"')")

    conn.commit()
    
    conn.close()

    print("account created")

def sql_confirmUser(data):
    conn = sqlite3.connect('server.db')

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE username='"+data['username']+"'")
    values = cursor.fetchone()

    conn.commit()
    conn.close()

    print(values)

    real_password = values[3]

    if real_password == data["password"]:
        new_data = {
            "first_name": values[0],
            "last_name": values[1],
            "username": values[2],
            "email": values[4],
            "uuid": values[5],
            "userType": values[6]
        }

        return new_data
    else:
        return {"real_account": False}

@app.get('/')
def connecting_server():
    return {"connected": True}


@app.post('/registerPlayerUser')
def create_user(user: User):
    new_uuid = uuid.uuid4()

    data = {
        'first_name': user.fname,
        'last_name': user.lname,
        'username': user.username,
        'password': user.password,
        'email': user.email,
        'uuid': str(new_uuid),
        'userType': user.userType
    }

    print(data)
    sql_createUser(data)

    return data

@app.post("/confirmPlayerUser")
def confirm_user(con_user: Con_User):
    data = {
        "username": con_user.username,
        "password": con_user.password
    }

    print(data)

    find_account = sql_confirmUser(data)

    return find_account