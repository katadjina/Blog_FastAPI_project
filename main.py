from fastapi import FastAPI
from database import models
from database.database import engine

app = FastAPI()

@app.get("/")
def test():
    return "Hello"

models.Base.metadata.create_all(engine)
