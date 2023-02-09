from fastapi import FastAPI
import shutil
import os
from pydantic import BaseModel
import string2image

class ClientData(BaseModel):
     texts: str

app=FastAPI()

@app.post("/")
async def root(text: ClientData):
    string2image.string2image(text.texts)
    return {"class":"OK"}