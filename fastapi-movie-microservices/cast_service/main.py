from fastapi import FastAPI

# router codes
from api.cast import cast_route
from api import db

app = FastAPI()


app.include_router(cast_route, prefix="/api/v1/cast", tags=["cast"])


@app.on_event("startup")
async def startup_event():
    # try to connect to db
    try:
        # await db.database.connect()
        pass
    except Exception as e:
        print(e)
        raise e
    
# on shutdown event ~ close db connection
@app.on_event("shutdown")
async def shutdown_event():
    # try to close db connection
    try:
        # await db.database.disconnect()
        pass
    except Exception as e:
        print(e)
        raise e