from fastapi import APIRouter, status
from schemas import pyd_schemas
from crud import continent
from typing import List
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

@router.get("/get_all", response_model=List[pyd_schemas.Continent], status_code=status.HTTP_200_OK)
def get_all_continents():
    task = continent.get_all_continent.apply_async()
    result = task.wait(timeout=None, interval=0.5)
    return result

@router.post("/add")
async def add_new_continent(request: pyd_schemas.Continent):
    task_id = continent.add_new_continent.apply_async(args=[request])
    return JSONResponse(status_code=status.HTTP_202_ACCEPTED, content={"task_id": str(task_id)})
