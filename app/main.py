from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import uuid

app = FastAPI(
    title="FastAPI Demo Service",
    description="A simple API service ready for ECS deployment",
    version="0.1.0"
)

# Simple in-memory database
items_db = {}

class Item(BaseModel):
    id: Optional[str] = None
    name: str
    description: Optional[str] = None
    price: float

class ItemResponse(Item):
    id: str

@app.get("/")
async def root():
    return {"message": "Welcome to FastAPI Demo Service"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.post("/items/", response_model=ItemResponse, status_code=201)
async def create_item(item: Item):
    item_id = str(uuid.uuid4())
    item_dict = item.dict()
    item_dict["id"] = item_id
    items_db[item_id] = item_dict
    return item_dict

@app.get("/items/", response_model=List[ItemResponse])
async def read_items():
    return list(items_db.values())

@app.get("/items/{item_id}", response_model=ItemResponse)
async def read_item(item_id: str):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return items_db[item_id]

@app.put("/items/{item_id}", response_model=ItemResponse)
async def update_item(item_id: str, item: Item):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    
    item_dict = item.dict(exclude_unset=True)
    item_dict["id"] = item_id
    items_db[item_id] = item_dict
    return item_dict

@app.delete("/items/{item_id}", status_code=204)
async def delete_item(item_id: str):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    
    del items_db[item_id]
    return None
