import os
from sqlalchemy import (Column, Integer, MetaData, String, Table,
    create_engine, ARRAY)
from databases import Database

# from dotenv import load_dotenv
# load_dotenv()

# manage connection with database
# print(os.environ.get('TEST_ENV'))

# DATABASE_NAME = os.environ.get('DATABASE_NAME')
# DATABASE_PASSWORD = os.environ.get('DATABASE_PASSWORD')

DATABASE_URL= f"postgresql://postgres:mea4545Luda@localhost/movies_microservice_db"

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