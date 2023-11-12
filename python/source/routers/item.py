from fastapi import APIRouter
from models.item import Item
import uuid

router = APIRouter(
    prefix="/item",
    tags=["item"]
)



@router.post("/")
async def create_item(item: Item):

    return {"message": item}


@router.get("/{id}")
async def get_item(id: str):

    return {"message": "Item retrieved successfully"}


@router.put("/{id}")
async def update_item(id: str, item: Item):

    return {"message": "Item updated successfully"}


@router.delete("/{id}")
async def delete_item(id: str):


    return {"message": "Item deleted successfully"}


@router.get("/")
async def get_all_items():

    return {"message": "All items retrieved successfully"}
