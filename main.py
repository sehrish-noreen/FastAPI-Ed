from fastapi import FastAPI, HTTPException, status
import json

def load_data():
    with open("colors.json", "r") as file:
        data = json.load(file)
        return data

app = FastAPI()

@app.get("/")
def root():
    return {"message": "welcome to ColorsInfo"}

@app.get("/colors")
def show_colors():
    return load_data()

@app.get("/colors/{color_name}")
def show_onecolor(color_name: str):
    data = load_data()
    for color in data["colors"]:
        if color["name"].lower() == color_name:
            return color

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="color not found")
