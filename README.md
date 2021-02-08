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

---
## Key Points
Read the [docs](https://fastapi.tiangolo.com/tutorial/).

1. Important [first steps](https://fastapi.tiangolo.com/tutorial/first-steps/).

2. Path parameters are always required - cannot be optional.

3. Order of the `get` methods matter.

    Example: Because path operations are evaluated in order, you need to make sure that the path for `/users/me` is declared before the one for `/users/{user_id}`. Otherwise, the path for `/users/{user_id}` would match also for `/users/me`, "thinking" that it's receiving a parameter `user_id` with a value of `"me"`.

4. Query parameters can be optional.

5. The `Optional[...]` library is only used by the editor to help find errors in your code. It is not required by FastAPI.

6. Non-default arguments to a function cannot be declared after arguments with defaults. i.e,:
    ```python
    def func(x='something', y='randomValue', a, b):
        pass
    ```
    The above function definition throws a SyntaxError. You can instead do something like this:
    ```python
    def func(a, b, x='something', y='randomValue'):
        pass
    ```
