from fastapi import FastAPI
import logging

logging.basicConfig(level=logging.INFO, format='%(levelname)s:     %(message)s')

app = FastAPI(title="backend")

@app.get("/")
async def hello():
    logging.info('hello')
    return {"message": "hello"}
