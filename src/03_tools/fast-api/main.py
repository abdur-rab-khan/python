from typing import Annotated

from fastapi.applications import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: bool | None = None


@app.get("/")
def read_root():
    return {"Hello": "Python"}


@app.get("/items/{item_id}")
def read_item(item_id: str, q: str | None = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(
    item_id: str, item: Item, q: Annotated[str, Field(min_length=3, max_length=20)]
):
    return {
        "query": q,
        "item_id": item_id,
        "price": item.price,
        "item_name": item.name,
        "is_offer": item.is_offer,
    }
