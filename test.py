from fastapi import FastAPI
import json

def load_json():
    with open("sample1.json", 'r') as file:
        data = json.load(file)
        return data

app = FastAPI()

@app.get('/')
def test():
    return {"message": "this is test program"}

@app.get('/data')
def retrieve_data():
    return load_json()
