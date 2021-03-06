from datetime import datetime
from pathlib import Path
from typing import Optional, Union

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

current_dir = Path(__file__).parent.absolute()
app.mount("/static", StaticFiles(directory=current_dir.joinpath("static")), name="static")


def timestamp(value: Optional[Union[datetime, int]], format_: str = "%Y-%m-%d %H:%M:%S") -> str:
    if isinstance(value, datetime):
        return value.strftime(format_)
    if isinstance(value, int):
        return datetime.fromtimestamp(value).strftime(format_)
    return ""


templates = Jinja2Templates(directory=current_dir.joinpath("templates"))
templates.env.filters["timestamp"] = timestamp


@app.get("/")
async def read_item(request: Request):
    return templates.TemplateResponse("index.j2", {"created_at": datetime.utcnow(), "request": request})
