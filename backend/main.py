from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, EmailStr

import os
from dotenv import load_dotenv
load_dotenv()

from motor.motor_asyncio import AsyncIOMotorClient

app = FastAPI()

#allow request from frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#MongoDB setup
uri = os.getenv("Mongodb_conn")

# Create a new client and connect to the server
client = AsyncIOMotorClient(uri)
db = client["Contact_details"]
Contact_details = db["Contact_detail"]

class contact_detail(BaseModel):
    Name: str
    Email: EmailStr
    Message:str

@app.post("/contact")
async def get_contact_details(data:contact_detail):
    result = await Contact_details.insert_one({
        "Name": data.Name,
        "Email": data.Email,
        "Message": data.Message
    })
    if result.inserted_id:
        return {"success":True, "message":"Saved"}
    else:
        raise HTTPException(status_code = 500, detail="Failed to save")