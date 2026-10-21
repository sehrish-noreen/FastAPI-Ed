# ColorsInfo API

Educational FastAPI project demonstrating CRUD operations, Pydantic validation, and JSON file storage.

## Endpoints
<img width="1127" height="625" alt="image" src="https://github.com/user-attachments/assets/8b3b57db-68de-4154-8bb9-9edfa8a048b7" />

* **GET** `/` - Welcome message
* **GET** `/colors` - List all colors
* **GET** `/colors/{color_name}` - Show color by name
* **GET** `/sort_colors?sort_by=...` - Sort colors by (`name`, `hex`, `category`)

* **POST** `/add_color` - Add new color
* Payload:
    ```json
    {
      "name": "red",
      "hex": "#FF0000",
      "rgb": {"r": 255, "g": 0, "b": 0},
      "category": "primary"
    }
    ```
* **PUT** `/update_color?color_name=...` - Update color by name
  * Parameter: `/update_color?color_name=red`
  * Payload:
    ```json
    {
      "name": "crimson",
      "hex": "#DC143C",
      "rgb": {"r": 220, "g": 20, "b": 60},
      "category": "primary"
    }
    ```
* **DELETE** `/remove_color?color_name=...` - Delete color by name
  * Parameter: `/remove_color?color_name=red`

## Setup & Run

1. Install dependencies:
   ```bash
   pip install fastapi uvicorn pydantic
