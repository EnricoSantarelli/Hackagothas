from fastapi import FastAPI
from src.modules.delete_criminal_record.app.delete_criminal_record_presenter import delete_criminal_record_presenter
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
