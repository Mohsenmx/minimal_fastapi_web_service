import httpx
import time
import asyncio

endpoint_1 = "http://127.0.0.1:8080/input"
endpoint_2 = "http://127.0.0.1:8080/summarize"
value = 1
result = 10000
data = {"item": value}


async def send_task(endpoint, data):
    print("start coroutine")
    async with httpx.AsyncClient() as client:
        for i in range(200):
            await client.post(endpoint, json=data)

async def send_request(endpoint, data):
    start_time = time.time()
    tasks = []
    for i in range(50):
        task = asyncio.create_task(send_task(endpoint, data))
        tasks.append(task)
    for t in tasks:
        await t

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"{elapsed_time:.0f} seconds")

def get_response(endpoint, result):
    response = httpx.get(endpoint)
    recv_data = response.json()

    if recv_data['sum'] == result:
        print('OK')
    else:
        print('not OK')

if __name__ == "__main__":
    asyncio.run(send_request(endpoint_1, data))
    get_response(endpoint_2, result)