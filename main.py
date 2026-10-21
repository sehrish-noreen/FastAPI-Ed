from fastapi import FastAPI, HTTPException, status
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

# client data, create a new record
@app.post("/color", status_code=status.HTTP_201_CREATED)
def add_color(color: Color):
    data = load_data()
    new_color_dict = color.model_dump()
    data["colors"].append(new_color_dict)
    save_data(data)
    return {"message": "color added successfully", "color":new_color_dict}
