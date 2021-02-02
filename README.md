# FastAPI Practice

Learning FastAPI and Pydantic

## Setup
1. Clone this repository and open a terminal inside the directory.

2. Create a venv using python in your project's directory (recommended python3.8 and above).
    ```
    python3 -m venv venv
    ```

3. Activate the virtual environment.
    ```
    source venv/bin/activate
    ```
    You should see `(venv)` before your prompt in the terminal.

4. Download all required python packages.
    ```
    python3 -m pip install -r requirements.txt
    ```

5. Start the FastAPI server.
    ```
    uvicorn main:my_app --reload
    ```
    The server will be started in `localhost:8000`. You can access your API by going to `localhost:8000/docs` or `localhost:8000/redoc`.