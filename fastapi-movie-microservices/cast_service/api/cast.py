from fastapi import APIRouter



cast_route = APIRouter()


@cast_route.get("/cast_test")
async def get_cast():
    return {"cast": "cast_test"}