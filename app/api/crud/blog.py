from app.api.models.blog import BlogSchema
from app.db import blogs, database

async def post(payload: BlogSchema):
    query = blogs.insert().values(title=payload.title, description=payload.description)
    return await database.execute(query)

async def get(id: int):
    query = blogs.select().where(id == blogs.c.id)
    return await database.fetch_one(query)
    

async def get_all():
    query = blogs.select()
    return await database.fetch_all(query)


async def put(id:int, payload=BlogSchema):
    query = (
        blogs.update().where(id == blogs.c.id).values(title=payload.title, description=payload.description)
        .returning(blogs.c.id)
    )
    return await database.execute(query)

async def delete(id:int):
    query = blogs.delete().where(id == blogs.c.id)
    return await database.execute(query)
    