from typing import Any, List
from fastapi import APIRouter, HTTPException, Path, FastAPI

from app.api.crud import blog
from app.api.models.blog import BlogSchema,BlogDB

router = APIRouter()


@router.post("/", response_model=BlogDB, status_code=201)
async def create_blog(payload: BlogSchema):
    note_id = await blog.post(payload)

    response_object = {
        "id": note_id,
        "title": payload.title,
        "description": payload.description,
    }
    return response_object
    
@router.get("/{id}/", response_model=BlogDB)
async def read_blog(id: int = Path(..., gt=0),):
    note = await blog.get(id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    return note

@router.get("/", response_model=List[BlogDB])
async def read_all_blogs():
    return await blog.get_all()

@router.put("/{id}/", response_model=BlogDB)
async def update_blog(payload:BlogSchema,id:int=Path(...,gt=0)): #Ensures the input is greater than 0
    note = await blog.get(id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    note_id = await blog.put(id, payload)
    response_object = {
        "id": note_id,
        "title": payload.title,
        "description": payload.description
    }
    return response_object

#DELETE route
@router.delete("/{id}/", response_model=BlogDB)
async def delete_blog(id:int = Path(...,gt=0)):
    note = await blog.get(id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    await blog.delete(id)

    return note
