from fastapi import FastAPI
from pydantic import BaseModel, root_validator

app = FastAPI()


class WithRootValidatorParams(BaseModel):
    name: str

    @root_validator
    def validate(cls, values: dict):
        return values


class WithoutRootValidatorParams(BaseModel):
    name: str


@app.post("/with-root-validator")
async def test1(params: WithRootValidatorParams):
    return str(type(params))


@app.post("/without-root-validator")
def test2(params: WithoutRootValidatorParams):
    return str(type(params))
