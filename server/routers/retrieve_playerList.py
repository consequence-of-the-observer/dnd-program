from fastapi import APIRouter
from pydantic import BaseModel

import sqlite3
import uuid

router = APIRouter()

class CampaignId(BaseModel):
    id: str


def sql_getPlayerList(data):
    conn = sqlite3.connect("server.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM player_in_campaign WHERE campaign_id='"+data+"'")
    values = cursor.fetchall()
    print(values)

    user_list = []

    for x in values:
        y = x[0]
        print(y)
        cursor.execute("SELECT * FROM users WHERE uuid='"+y+"'")
        user_values = cursor.fetchone()
        print(user_values)
        user_data = {
            "userid": user_values[2]
        }

        user_list.append(user_data)

    conn.commit()
    conn.close()
    return user_list

@router.post("/retrievePlayerList")
def getPlayerList(campaign: CampaignId):
    data = sql_getPlayerList(campaign.id)

    return data