# ColorsInfo API

Educational FastAPI project: CRUD operations, Pydantic validation, and JSON file storage.

## Endpoints

<img width="1127" height="625" alt="image" src="https://github.com/user-attachments/assets/8b3b57db-68de-4154-8bb9-9edfa8a048b7" />

- **GET** `/` - Welcome message
- **GET** `/colors` - List all colors
- **GET** `/colors/{color_name}` - Show color by name
  - Example: `/colors/red`
- **GET** `/sort_colors` - Sort colors by field (`name`, `hex`, or `category`)
  - Example: `/sort_colors?sort_by=name`
- **POST** `/add_color` - Add new color
  - Payload:
    ```json
    {
      "name": "red",
      "hex": "#FF0000",
      "rgb": { "r": 255, "g": 0, "b": 0 },
      "category": "primary"
    }
    ```
- **PUT** `/update_color` - Update color by name
  - Query parameter: `/update_color?color_name=red`
  - Payload:
    ```json
    {
      "name": "crimson",
      "hex": "#DC143C",
      "rgb": { "r": 220, "g": 20, "b": 60 },
      "category": "primary"
    }
    ```
- **DELETE** `/remove_color` - Delete color by name
  - Query parameter: `/remove_color?color_name=red`

## Setup & Run

1. Install dependencies:
   ```bash
   pip install fastapi uvicorn pydantic uv
   ```

2. Create `colors.json` in the project root (add some initial data optional):
   ```json
   {
     "colors": []
   }
   ```

3. Run the server:
   ```bash
   uv run fastapi dev
   ```
