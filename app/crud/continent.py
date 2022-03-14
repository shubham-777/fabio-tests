from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from models import sql_models
from schemas import pyd_schemas
from celery_worker.crud_worker import app
from database.mysql import SessionLocal
import time

@app.task(name='celery_tasks.tasks.get_all_continents')
def get_all_continent():
    db = SessionLocal()
    try:
        llst_continents = db.query(sql_models.Continent).all()
        time.sleep(60)
        return pyd_schemas.Continent.from_orm_list(llst_continents)
    except Exception:
        raise
    finally:
        db.close()

@app.task(name='celery_tasks.tasks.add_continent')
def add_new_continent(request: pyd_schemas.Continent):
    db = SessionLocal()
    try:
        entry_exists = db.query(sql_models.Continent.id).filter_by(name=request.name).first()
        if entry_exists:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"Continent with continent_name:{request.name} already exist")
        lobj_continent = sql_models.Continent(name=request.name, population=request.population, area=request.area)
        db.add(lobj_continent)
        db.commit()
        db.refresh(lobj_continent)
        return pyd_schemas.Continent.from_orm(lobj_continent)
    except Exception:
        raise
    finally:
        db.close()
        