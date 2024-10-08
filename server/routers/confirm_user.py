from fastapi import APIRouter
from pydantic import BaseModel

import sqlite3
import uuid

router = APIRouter()

class Con_User(BaseModel):
    username: str
    password: str

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

@router.post("/confirmPlayerUser")
def confirm_user(con_user: Con_User):
    data = {
        "username": con_user.username,
        "password": con_user.password
    }

    print(data)

    find_account = sql_confirmUser(data)

    return find_account