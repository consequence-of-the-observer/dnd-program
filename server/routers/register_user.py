from fastapi import APIRouter
from pydantic import BaseModel

import sqlite3
import uuid

router = APIRouter()

class User(BaseModel):
    fname: str
    lname: str
    username: str
    password: str
    email: str
    userType: str

def sql_createUser(data):
    conn = sqlite3.connect('server.db')

    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS users
                    (first_name, last_name, username, password, email, uuid, userType)''')
    cursor.execute("INSERT INTO users VALUES ('"+data['first_name']+"','"+data['last_name']+"','"+data['username']+"','"+data['password']+"','"+data['email']+"','"+data['uuid']+"', '"+data['userType']+"')")

    conn.commit()
    
    conn.close()

    print("account created")

@router.post('/registerPlayerUser')
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