from fastapi import Request, HTTPException
from app import app
from utils import parse_query

@app.get("/execute")
async def execute(q: str):
    result = parse_query(q)
    if result:
        return result
    raise HTTPException(status_code=400, detail="Query not recognized.")
