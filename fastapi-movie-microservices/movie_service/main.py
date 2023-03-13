from fastapi import FastAPI

# get movies api router
from .api.movies import movie
from .api.db import metadata,database,engine

metadata.create_all(engine)

app = FastAPI()

# on startup connect to database 
@app.on_event("startup")
async def startup():
    try:
        await database.connect()
        print("--------- DB connection success ----------")
    except ConnectionRefusedError as e:
        print(e)

# on shutdown disconect from db
@app.on_event("shutdown")
async def shutdown():
    try:
        await database.disconnect()
        print("--------- DB diconeconnection success ----------")
    except ConnectionAbortedError as e:
        print(e) 

app.include_router(movie, prefix='/api/v1/movies', tags=['movies'])