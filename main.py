from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


my_app = FastAPI()

@my_app.get("/")
async def home():
    return {"message": "Hello there!"}


@my_app.get("/items/")
async def get_items():
    return {"message": "Pending work for get all items"}


@my_app.get("/items/{item_id}")
async def get_item_by_id(item_id: int):
    return {"item-id": item_id, "message": "Pending work for get item"}


@my_app.post("/items/")
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price * (1 + item.tax/100)
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict