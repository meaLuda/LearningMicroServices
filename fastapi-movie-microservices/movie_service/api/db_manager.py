from .models import MovieIn,MovieOut,MovieUpdate
from .db import movies,database

# manage databse queries to and from.
# add a movie
async def add_movie(payload:MovieIn):
    """
    
    """
    query = movies.insert().values(**payload.dict())
    return await database.execute(query=query)

# get all movies
async def get_all_moveis():
    """
        ## get all movies from the db
    """
    query = movies.select()
    return await database.fetch_all(query=query)

# get movie with id
async def get_movie(id):
    """
        ## get a movie from db by id
        movies.c.id ~ movie.column.id where column id has id == to our id
    """
    query = movies.select(movies.c.id==id)
    return await database.fetch_all(query=query)

# delete movie with id
async def delete_movie(id):
    query = movies.delete().where(
        movies.c.id==id
    )

    return await database.execute(query=query)

# update movie
async def update_movie(id:int,payload:MovieIn):
    query = (
        movies.\
            update().\
                where(movies.c.id==id).\
                    values(**payload.dict())
    )
    return await database.execute(query=query)

