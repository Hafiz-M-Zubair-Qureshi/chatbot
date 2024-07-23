from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import openai
from fastapi.middleware.cors import CORSMiddleware
import os 
from dotenv import load_dotenv
load_dotenv()


app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Message(BaseModel):
    message: str
    model: str

@app.post("/chat/{message}/")
async def chat(message: str): 
    try:
        client = openai.OpenAI()
        response = client.chat.completions.create(
            model='gpt-4o',
            messages=[{"role": "user", "content": message}]
        )
        return {"message": response.choices[0].message.content}
    except Exception as e:
        print(e)
        raise HTTPException( status_code=404 , detail=str(e))