import os
from sqlalchemy import (Column, Integer, MetaData, String, Table,
    create_engine, ARRAY)
from databases import Database

DATABASE_URL= "postgresql://postgres:mea4545Luda@localhost/movies_microservice_db"

try:
    engine=create_engine(DATABASE_URL)

    metadata= MetaData()

    # create table for movies
    movies = Table(
        'movies',
        metadata,
        Column('id', Integer, primary_key=True),
        Column('name', String(50)),
        Column('plot', String(250)),
        Column('genres', ARRAY(String)),
        Column('casts', ARRAY(String))
    )

    database=Database(DATABASE_URL)
except ConnectionError as e:
    print(e)