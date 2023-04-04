from fastapi import FastAPI
from src.modules.create_crime.app.create_crime_presenter import create_crime_presenter
from src.modules.delete_criminal_record.app.delete_criminal_record_presenter import delete_criminal_record_presenter
from src.modules.get_all_criminal_records.app.get_all_criminal_records_presenter import get_all_criminal_records_presenter
from src.modules.get_crimes_by_criminal_record_id.app.get_crimes_by_criminal_record_id_presenter import get_crimes_by_criminal_record_id_presenter
from src.modules.update_criminal_record.app.update_criminal_record_presenter import update_criminal_record_presenter

app = FastAPI()


@app.delete("/delete_criminal_record/")
def delete_criminal_record(data: dict = None):
    event = {
        "body": {
            k: str(v) for k, v in data.items()
        }
    }

    response = delete_criminal_record_presenter(event, None)
    return response


@app.put("/update_criminal_record/")
def update_criminal_record(data: dict = None):
    event = {
        "body": {
            k: str(v) for k, v in data.items()
        }
    }
    for key in data.keys():
        if type(data[key]) == dict:
            event["body"][key] = {
                k: str(v) for k, v in data[key].items()
            }
    response = update_criminal_record_presenter(event, None)
    return response


@app.get("/get_all_criminal_records/")
def get_all_criminal_records():
    event = {}

    response = get_all_criminal_records_presenter(event, None)
    return response


@app.post("/get_crimes_by_criminal_record_id/")
def get_crimes_by_criminal_record_id(data: dict = None):
    event = {
        "body": {
            k: str(v) for k, v in data.items()
        }
    }

    response = get_crimes_by_criminal_record_id_presenter(event, None)
    return response


@app.post("/create_crime/")
def create_crime(data: dict = None):
    event = {
        "body": {
            k: str(v) for k, v in data.items()
        }
    }
    for key in data.keys():
        if type(data[key]) == dict:
            event["body"][key] = {
                k: str(v) for k, v in data[key].items()
            }
    response = create_crime_presenter(event, None)
    return response
