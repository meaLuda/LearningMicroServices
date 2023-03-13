from typing import List
from fastapi import Header, APIRouter,HTTPException

from .models import MovieIn,MovieOut
from .db_manager import add_movie,get_movie,update_movie,delete_movie,get_all_moveis

movie = APIRouter()


# Fake movie db ~ testing
fake_movie_db = [
    {
        'name': 'Star Wars: Episode IX - The Rise of Skywalker',
        'plot': 'The surviving members of the resistance face the First Order once again.',
        'genres': ['Action', 'Adventure', 'Fantasy'],
        'casts': ['Daisy Ridley', 'Adam Driver']
    }
]


# root
@movie.get('/')
async def index():
    return {
        "Index":"Microservices with Python."
    }

# get all movies ~ GET REQ
@movie.get('/all_movies',response_model=List[MovieOut])
async def movies():
    # for test
    # return fake_movie_db

    # get data from db
    return await get_all_moveis()

# Add a movie to our test db ~ POST REQ
@movie.post('/add',status_code=201)
async def add_movie(payload:MovieIn):
    movie_id = await add_movie(payload)

    response = {
        'id': movie_id,
        **payload.dict()
    }

    return response

# update an existing movie
@movie.put('/{id}',status_code=200)
async def update_movie(id:int, payload:MovieIn):
   # take dictionary
   movie = await get_movie(id)

   if not movie:
      raise HTTPException(
           status_code=404,
           detail=f"Movie of id:{id} not found"
       )
   
   update_data = payload.dict(exclude_unset=True)

   movie_in_db = MovieIn(**movie)

   updated_movie_data = movie_in_db.copy(update=update_data)

   return await update_movie(id,updated_movie_data)
   

# delete an extisting item
@movie.delete('/{id}')
async def del_movie(id:int):
    # get len of movies in db
    movie = await get_movie(id)

    if not movie:
        raise HTTPException(status_code=404,detail=f"Movie with id:{id} not found")
    
    return await delete_movie(id)
    