from typing import Union
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.api.endpoints import blogs
#from app.api.api import api_router
from app.db import Base, engine, metadata, database

Base.metadata.create_all(engine)

app = FastAPI()
origins = [    
    "http://127.0.0.1:8000/",
    "http://localhost:8081",
    "http://localhost:8080",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["DELETE", "GET", "POST", "PUT"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup():
    await database.connect()  

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.get("/")
def read_root():
    return {"This is Python FastAPI blog application"}

app.include_router(blogs.router, prefix="/api/blogs", tags=["blogs"])
