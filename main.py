from fastapi import FastAPI, Query, Path
from pydantic import BaseModel
from typing import Optional, List

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
async def get_items(
    q: Optional[List[str]] = Query(
        None,
        title="Query q",
        description="Random description for q",
        max_length=50,
        alias="item-query",
        # 'item-query' is NOT a valid parameter variable
        # but can be used as an alias for 'q'
    ),
    z: list = Query(
        ["foo", "bar"],
        deprecated=True,
    )
):
    results = {
        "items": [
            {"item_id": 0, "item_name": "Set Dosa"},
            {"item_id": 1, "item_name": "Vada"},
        ]
    }
    try:
        results.update({
            "query q": q,
            "query z": z,
        })
    except Exception as e:
        message = f"Error occurred: {e}"
        print(message)
    
    return results


@my_app.get("/items/{item_id}")
async def get_item_by_id(
    q: str,
    item_id: int = Path(
        ...,  # Ellipsis - acts as placeholder and enforces requirement
        description="The id of the item to get",
        ge=1,  # item_id has to be an integer greater than or equal to 1
    ),
):
    return {"item-id": item_id, "message": "Pending work for get item"}


@my_app.post("/items/")
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price * (1 + item.tax/100)
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict