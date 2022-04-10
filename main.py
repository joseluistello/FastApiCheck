from fastapi import FastAPI

from enum import Enum
from pydantic import BaseModel

class Department(str, Enum):
    MATH = "math"
    ENGLISH = "english"
    CHEMISTRY = "chemistry"

app = FastAPI()


@app.get("/")
async def read_main():
    return {"message": "Hello World"}

@app.get("/employees/{employee_id}")
async def get_employees(employe_id: int, department: Department, gender: str = None):
    print(employe_id)
    print(department)
    print(gender)
    return [{"id": 1, "name": "Bob"}, {"id":2, "name": "Pedro"}]

