from fastapi import FastAPI
import asyncio

app = FastAPI()

@app.get("/")
def index():
    return "Main route: /wait_60_minutes"

@app.get("/wait_60_minutes")
async def wait_60_minutes():
    try:
        for i in range(0, 3600):
            print("Seconds: ",i)
            await asyncio.sleep(1)
    except KeyboardInterrupt:
        raise SystemExit()
    return "Time awaited"
