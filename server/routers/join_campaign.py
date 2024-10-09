from fastapi import APIRouter
from pydantic import BaseModel

import sqlite3
import uuid

router = APIRouter()

class FindCampaign(BaseModel):
    name: str
    code: str
    playerId: str

def sql_addToCampaign(data):
    conn = sqlite3.connect('server.db')

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM campaigns WHERE name='"+data["name"]+"'")
    values = cursor.fetchall()

    desired_campaign = 0

    print(values)

    for x in values:
        print(x)
        if x[2] == data['code']:
            desired_campaign = x
            print(desired_campaign)
        else:
            print("not the right campaign")

    cursor.execute('''CREATE TABLE IF NOT EXISTS player_in_campaign
                    (player_id, campaign_id)''')

    cursor.execute("INSERT INTO player_in_campaign VALUES ('"+data['playerId']+"','"+desired_campaign[0]+"')")

    conn.commit()
    conn.close()

    print("added player to campaign "+ desired_campaign[2])

@router.post("/joinCampaign")
def join_campaign(campaign: FindCampaign):
    data = {
        "name": campaign.name,
        "code": campaign.code,
        "playerId": campaign.playerId
    }

    print(data)

    sql_addToCampaign(data)

    return data