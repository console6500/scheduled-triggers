from fastapi import FastAPI
import logging

logging.basicConfig(level=logging.INFO)

app = FastAPI(title="backend")

@app.get("/")
async def hello():
    logging.info('hello')
    return {"message": "hello"}
