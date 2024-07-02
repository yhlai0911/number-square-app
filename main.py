from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class NumberInput(BaseModel):
    number: int

@app.get("/")
async def root():
    return {"message": "Welcome to the Number Square App"}

@app.post("/square")
async def square_number(input: NumberInput):
    result = input.number ** 2
    print(f"Received number: {input.number}, Result: {result}")
    return {"result": result}