from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# 更新 CORS 配置
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 明確允許 Live Server 的源
    allow_credentials=True,
    allow_methods=["*"],  # 允許所有 HTTP 方法
    allow_headers=["*"],  # 允許所有 headers
)

class NumberInput(BaseModel):
    number: int

@app.post("/square")
async def square_number(input: NumberInput):
    result = input.number ** 2
    print(f"Received number: {input.number}, Result: {result}")  # 添加日誌
    return {"result": result}

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="localhost", port=8000)