# ColorsInfo API

Educational FastAPI project demonstrating CRUD operations, Pydantic validation, and JSON file storage.

## Endpoints

* **GET** `/` - Welcome message
* **GET** `/colors` - List all colors
* **GET** `/colors/{color_name}` - Show color by name
* **GET** `/sort_colors?sort_by=...` - Sort colors by (`name`, `hex`, `category`)
* **POST** `/add_color` - Add new color record
* **PUT** `/update_color?color_name=...` - Update color info by color_name
* **DELETE** `/remove_color?color_name=...` - Delete color by name

## Setup & Run

1. Install dependencies:
   ```bash
   pip install fastapi uvicorn pydantic
