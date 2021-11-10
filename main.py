from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.post("/callback")
def read_root(body:dict):
    with open('output.txt', 'w') as f:
        print(body,file=f)
    return body
