from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()


@app.get("/")
async def root():
    return FileResponse('index.html')

@app.post("/calc/")
async def calc(num1, num2):
    return {"result": sum([int(num1), int(num2)])}

@app.get("/custom")
def read_custom_message():
    return {"message": "This is a custom message!"}