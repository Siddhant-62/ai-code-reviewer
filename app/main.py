from fastapi import FastAPI
from pydantic import BaseModel
from app.reviewer import analyze_code

app = FastAPI()

class CodeInput(BaseModel):
    code: str

@app.post("/review/")
async def review_code(input: CodeInput):
    suggestions = analyze_code(input.code)
    return {"suggestions": suggestions}
