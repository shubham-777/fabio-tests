from fastapi import APIRouter, status
from schemas import pyd_schemas
from crud import continent
from fastapi.responses import JSONResponse

router = APIRouter(prefix="/continent", tags=["continent"], responses={404: {"description": "Not found"}})
tags_metadata = [
    {
        "name": "continent",
        "description": "CRUD operations related to **continent**.",
    }
]



#==============================
# continent
#==============================
# @router.get("/get_all",)
# def get_all_continents():
#     a = continent.get_all_continent()
#     return "ggreat"

@router.get("/get_all",)
def get_all_continents():
    task_id = continent.get_all_continent.apply_async()
    return JSONResponse(status_code=status.HTTP_202_ACCEPTED, content={"task_id": str(task_id)})

@router.post("/add")
async def add_new_continent(request: pyd_schemas.Continent):
    task_id = continent.add_new_continent.apply_async(request)
    return JSONResponse(status_code=status.HTTP_202_ACCEPTED, content={"task_id": str(task_id)})
