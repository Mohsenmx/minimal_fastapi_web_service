from fastapi import FastAPI
import asyncio

app = FastAPI()
db = []


async def async_input(item):
    db.append(item['item'])

@app.post('/input')
async def input_item(item: dict):
    await asyncio.create_task(async_input(item))
    return {}

@app.get('/summarize')
def summarize():
    global db
    result = sum(db)
    db = []
    return {'sum': result}


