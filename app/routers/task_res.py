from fastapi import APIRouter, status
from schemas import pyd_schemas
from crud import continent
from fastapi.responses import JSONResponse
from celery.result import AsyncResult
from celery_worker.crud_worker import app

router = APIRouter(prefix="/task_result", tags=["task_result"], responses={404: {"description": "Not found"}})
tags_metadata = [
    {
        "name": "task_result",
        "description": "get task result for its respective **task_id**.",
    }
]

@router.get("/{task_id}")
def get_task_result(task_id: str):
    task_result = AsyncResult(task_id, app=app)
    if task_result.ready():
        return JSONResponse(status_code=status.HTTP_200_OK, content=task_result.result)
    else:          
        result = {
            "task_id": task_id,
            "task_status": task_result.status
        }
        return JSONResponse(status_code=status.HTTP_200_OK, content=result)

