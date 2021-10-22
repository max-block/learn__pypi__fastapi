from fastapi import FastAPI
from starlette.responses import PlainTextResponse

app = FastAPI()


@app.get("/", response_class=PlainTextResponse)
def index():
    return "plain\ntext"
