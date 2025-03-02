# Ski Wax API

This project is a FastAPI-based web service for managing a database of ski waxes. It allows users to perform CRUD operations on ski wax data, including adding, updating, retrieving, and deleting wax records.

## Features

- **GET** `/waxes`: Retrieve all waxes
- **GET** `/waxes/{wax_id}`: Retrieve a specific wax by ID
- **POST** `/waxes`: Add a new wax
- **PUT** `/waxes/{wax_id}`: Update an existing wax
- **DELETE** `/waxes/{wax_id}`: Delete a specific wax by ID
- **DELETE** `/waxes`: Delete all waxes
- **POST** `/seed`: Seed the database with initial data

## Setup

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/wax_db.git
    cd wax_db
    ```

2. **Create a virtual environment and activate it:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the FastAPI application:**
    ```bash
    uvicorn api:app --reload
    ```

5. **Access the API documentation:**
    Open your browser and navigate to `http://127.0.0.1:8000/docs` to view the interactive API documentation provided by Swagger UI.

## Database

The database used in this project is SQLite. The database file `waxes.db` will be created automatically when you run the application for the first time.

## Seeding the Database

To seed the database with initial data, send a POST request to the `/seed` endpoint. This will populate the `ski_waxes` table with some sample data.

## Example Requests

- **Retrieve all waxes:**
    ```bash
    curl -X 'GET' \
      'http://127.0.0.1:8000/waxes' \
      -H 'accept: application/json'
    ```

- **Add a new wax:**
    ```bash
    curl -X 'POST' \
      'http://127.0.0.1:8000/waxes' \
      -H 'accept: application/json' \
      -H 'Content-Type: application/json' \
      -d '{
      "brand": "Swix",
      "model": "V40 Blue Extra",
      "wax_type": "Hard Wax",
      "temp_range": "-1°C to -7°C",
      "snow_type": "New or fine-grained snow",
      "notes": "Ideal for typical winter conditions; widely used for its versatility."
    }'
    ```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.