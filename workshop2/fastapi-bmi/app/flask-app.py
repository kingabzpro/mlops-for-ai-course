from fastapi import FastAPI
from custom_function import bmi

app = FastAPI()


@app.get("/")
def read_main():
    return {"message": "Welcome"}


@app.get("/bmi")
def read_item(height: int, weight: int):

    return {"BMI": bmi(height, weight)}
