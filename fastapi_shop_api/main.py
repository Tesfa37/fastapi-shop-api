from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Shop API 🛒")


class Item(BaseModel):
    id: int
    name: str
    price: float


DB: dict[int, Item] = {}  # in-memory fake DB


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/items", status_code=201)
def create_item(item: Item):
    DB[item.id] = item
    return item


@app.get("/items/{item_id}")
def read_item(item_id: int):
    if item_id not in DB:
        raise HTTPException(status_code=404, detail="Item not found")
    return DB[item_id]
