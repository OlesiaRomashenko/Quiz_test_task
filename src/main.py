from fastapi import FastAPI
from endpoints import router
from config import Settings
from db import connect

app = FastAPI(**Settings().model_dump())

app.include_router(router, prefix="/api")


@app.on_event('startup')
def start_event():
    with connect.cursor() as c:
        c.execute(
            "CREATE TABLE IF NOT EXISTS quiz_question (id INT PRIMARY KEY, question TEXT, answer TEXT, created_date TIMESTAMP)")
        connect.commit()
