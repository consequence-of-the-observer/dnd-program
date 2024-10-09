from fastapi import APIRouter
from pydantic import BaseModel

import sqlite3
import uuid

router = APIRouter()

class UserId(BaseModel):
    id: str

def sql_getPlayerCampaignList(data):
    conn = sqlite3.connect('server.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM player_in_campaign WHERE player_id='"+data+"'")
    values = cursor.fetchall()

    campaign_data = []

    for x in values:
        y = x[1]
        cursor.execute("SELECT * FROM campaigns WHERE id='"+y+"'")
        c_values = cursor.fetchone()
        c_data = {
            "id": c_values[0],
            "name": c_values[1],
            "gmId": c_values[3]
        }

        campaign_data.append(c_data)

    return campaign_data

@router.post("/playerCampaignList")
def playerCampaignList(user: UserId):
    data = sql_getPlayerCampaignList(user.id)

    return data