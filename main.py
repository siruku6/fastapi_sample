from typing import Optional
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def hello():
    return {"text": "hello world!"}


@app.get('/get/{path}') # methodとendpointの指定
async def path_and_query_params(
    path: str,
    # query: int,
    default_none: Optional[str] = None
):
    return {"text": f"hello, {path} and {default_none}"}
