from fastapi import APIRouter
from pydantic import BaseModel

import sqlite3
import uuid

router = APIRouter()

class UserId(BaseModel):
    id: str

def sql_getGameMasterCampaignList(data):
    conn = sqlite3.connect('server.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM campaigns WHERE gmId='"+data+"'")
    values = cursor.fetchall()

    campaign_data = []

    for x in values:
        c_values = x
        c_data = {
            "id": c_values[0],
            "name": c_values[1],
            "gmId": c_values[3]
        }

        campaign_data.append(c_data)

    return campaign_data

@router.post("/gameMasterCampaignList")
def playerCampaignList(user: UserId):
    data = sql_getGameMasterCampaignList(user.id)

    return data