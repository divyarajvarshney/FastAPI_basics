from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# In-memory database (for demonstration)
items = []

# Pydantic model for item data
class Item(BaseModel):
    name: str
    description: str

# Create an item
@app.post("/items", response_model=Item)
async def create_item(item: Item):
    """
    Adds a new item to the in-memory database.
    """
    items.append(item)
    return item

# Read an item
@app.get("/items/{item_id}", response_model=Item)
async def read_item(item_id: int):
    """
    Retrieves an item by its ID.
    Raises 404 error if the item is not found.
    """
    if item_id < 0 or item_id >= len(items):
        raise HTTPException(status_code=404, detail="Item not found")
    return items[item_id]

# Update an item
@app.put("/items/{item_id}", response_model=Item)
async def update_item(item_id: int, item: Item):
    """
    Updates an existing item in the in-memory database.
    Raises 404 error if the item is not found.
    """
    if item_id < 0 or item_id >= len(items):
        raise HTTPException(status_code=404, detail="Item not found")
    items[item_id] = item  # Update the item in the database
    return item
