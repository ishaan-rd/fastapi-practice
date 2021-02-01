from fastapi import FastAPI

my_app = FastAPI()

@my_app.get("/")
async def home():
    return {"message": "Hello there!"}


@my_app.get("/items/{item_id}")
async def get_item_by_id(item_id):
    return {"item-id": item_id}