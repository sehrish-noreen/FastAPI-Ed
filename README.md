# ColorsInfo API

Educational FastAPI project demonstrating CRUD operations, Pydantic validation, and JSON file storage.

## Endpoints
<img width="1127" height="625" alt="image" src="https://github.com/user-attachments/assets/8b3b57db-68de-4154-8bb9-9edfa8a048b7" />

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
