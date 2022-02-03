from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

health_route = APIRouter(prefix="/health", tags=["health"], responses={404: {"description": "Not found"}})

tags_metadata = [
    {
        "name": "health",
        "description": "api's related to service health",
    }
]

@health_route.get("/heartbeat")
async def check_health():
    return JSONResponse(status_code=status.HTTP_200_OK, content={"health": "all_good!"})