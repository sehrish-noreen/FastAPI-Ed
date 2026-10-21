from fastapi import FastAPI, HTTPException, status, Query
import json
from pydantic import BaseModel

# data model for validation of incoming data
class Color(BaseModel):
    name: str
    hex: str
    rgb: dict
    category: str

# load data
def load_data():
    try:
        with open("colors.json", "r") as file:
            data = json.load(file)
            return data
    except (FileNotFoundError, json.JSONDecodeError):
        return {"colors": []}

# save incoming client data
def save_data(data):
    with open("colors.json", "w") as file:
        json.dump(data, file, indent=4)

# init fastapi instance
app = FastAPI()

# root api endpoint, home
@app.get("/")
def root():
    return {"message": "welcome to ColorsInfo"}

# show all colors available
@app.get("/colors")
def show_colors():
    return load_data()

# get specific color using name
@app.get("/colors/{color_name}")
def show_onecolor(color_name: str):
    data = load_data()
    for color in data["colors"]:
        if color["name"].lower() == color_name.lower():
            return color
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="color not found")

# query parameters
@app.get("/sort_colors")
def sort_colors(sort_by:str |None  = Query(..., description="sort colors with given query", max_length=50)):
    data = load_data()
    fields = ["name", "hex", "category"]
    if sort_by not in fields:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="sort_by not found")
    sorted_data = sorted(data["colors"], key=lambda x:str(x.get(sort_by, 0)).lower(), reverse=False)
    return sorted_data

# client data, create a new record
@app.post("/add_color", status_code=status.HTTP_201_CREATED)
def add_color(color: Color):
    data = load_data()
    new_color_dict = color.model_dump()
    if new_color_dict not in data["colors"]:
        data["colors"].append(new_color_dict)
        save_data(data)
    else:
        return {"message": "color already exists"}

    return {"message": "color added successfully", "color":new_color_dict}
