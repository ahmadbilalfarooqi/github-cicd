from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World1", }


@app.get("/")
def read_root1():
    return {"Hello": "World2", }
