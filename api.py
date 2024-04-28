from fastapi import FastAPI
from starlette.responses import JSONResponse
import json
import csv

app = FastAPI()

@app.get("/")
async def homepage():
    return JSONResponse({'hello': 'world'})

@app.get("/points/{point_id}")
async def read_item(point_id: int):
    with open(f"reformed_data/{point_id}.json", "r") as fin:
        res = json.load(fin)
        opa = json.dumps(res)
        return JSONResponse(json.dumps(res))
    
@app.get("/database")
async def get_database():
    with open("database.csv", "r") as fin:
        csv_reader = csv.DictReader(fin)
        json_data = [row for row in csv_reader]
        return JSONResponse(json_data)
        #return json.load(fin)