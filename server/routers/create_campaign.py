from fastapi import APIRouter
from pydantic import BaseModel

import sqlite3
import uuid

router = APIRouter()

class Campaign(BaseModel):
    name: str
    code: str
    gmId: str

def sql_createCampaign(data):
    conn = sqlite3.connect('server.db')
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS campaigns
                    (id, name, code, gmId)''')

    cursor.execute("INSERT INTO campaigns VALUES ('"+data["id"]+"','"+data["name"]+"','"+data["code"]+"','"+data["gmId"]+"')")


    conn.commit()

    conn.close()
    print("campaign created")

@router.post("/createNewCampaign")
def create_campaign(campaign: Campaign):
    new_uuid = uuid.uuid4()
    data = {
        "id": str(new_uuid),
        "name": campaign.name,
        "code": campaign.code,
        "gmId": campaign.gmId
    }

    print(data)

    sql_createCampaign(data)

    return data