import random
import time

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def index():
    rand = random.randint(1, 9_999_999)
    print(f"start: {rand}")
    time.sleep(5)  # it blocks!
    print(f"stop: {rand}")
    return "done"
