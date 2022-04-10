from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/employees/{employee_id}")
async def get_employees(employe_id: int):
    return [{"id": 1, "name": "Bob"}, {"id":2, "name": "Pedro"}]