from fastapi import FastAPI
from starlette.responses import StreamingResponse
import asyncio


app = FastAPI()


@app.get("/")
def index():
    return "Main route: /wait_60_minutes"
async def wait_60_minutes():
    try:
        for i in range(0, 3600):
            print("Seconds: ",i)
            await asyncio.sleep(1)
            yield f"{i}\n"
    except KeyboardInterrupt:
        raise SystemExit()


@app.get("/wait_60_minutes")
async def streaming_response():
    return StreamingResponse(wait_60_minutes(), media_type="text/plain")




