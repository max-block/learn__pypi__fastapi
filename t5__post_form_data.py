from decimal import Decimal

from fastapi import FastAPI, Form

app = FastAPI()


@app.post("/test")
def test(amount: Decimal = Form(...), name: str = Form(...)):
    return {"amount": amount, "name": name}


# xh post :3000/test -f name=n1 amount=32
