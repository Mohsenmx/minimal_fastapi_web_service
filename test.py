import httpx
import time
import asyncio

endpoint_1 = "http://127.0.0.1:8000/input"
endpoint_2 = "http://127.0.0.1:8000/summarize"
value = 1
result = 100000
data = {'item': value}

async def async_send(endpoint, data):
    async with httpx.AsyncClient() as client:
        try:
            print('start task')
            for _ in range(25000):
                await client.post(endpoint, json=data)
        except:
            print('error occured')
    
async def send_request(endpoint, data):
    tasks = []
    for _ in range(4):
        task = asyncio.create_task(async_send(endpoint, data))
        tasks.append(task)
    await asyncio.gather(*tasks)


def get_response(endpoint, result):
    response = httpx.get(endpoint)
    recv_data = response.json()

    if recv_data['sum'] == result:
        print('OK')
    else:
        print('not OK')
    print(recv_data)

if __name__ == "__main__":
    start_time = time.time()
    asyncio.run(send_request(endpoint_1, data))
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"{elapsed_time:.0f} seconds")

    get_response(endpoint_2, result)