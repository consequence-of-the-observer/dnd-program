from fastapi import FastAPI 
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from routers import register_user, confirm_user, create_campaign, join_campaign, player_campaignList
import sqlite3
import uuid

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get('/')
def connecting_server():
    return {"connected": True}

app.include_router(register_user.router)
app.include_router(confirm_user.router)
app.include_router(create_campaign.router)
app.include_router(join_campaign.router)
app.include_router(player_campaignList.router)