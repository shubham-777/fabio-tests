from sys import prefix
from fastapi import FastAPI
import uvicorn
from fastapi.exception_handlers import http_exception_handler
from routers import continent, country, city
from models import sql_models
from routers import health
from database import mysql

description = """
A Python REST API 🚀

## Usage

lorem ipsum **lorem ipsum lorem ipsum lorem ipsum **.
lorem ipsum **lorem ipsum lorem ipsum lorem ipsum **.

## Changelog
 - lorem ipsum
"""
author = "Shubham Ahinave"
all_tags_metadata = list()
all_tags_metadata.extend(health.tags_metadata)
all_tags_metadata.extend(continent.tags_metadata)
all_tags_metadata.extend(country.tags_metadata)
all_tags_metadata.extend(city.tags_metadata)

app = FastAPI( title="Wiki API",
    prefix="wiki",
    description=description,
    version="1.0.0",
    contact={
        "name": "Shubham Ahinave",
        "url": "https://github.com/shubham-777",
        "email": "codesign.developers@gmail.com",
    },openapi_tags=all_tags_metadata)

sql_models.Base.metadata.create_all(bind=mysql.engine)
app.include_router(health.health_route)
app.include_router(continent.router)
app.include_router(country.router)
app.include_router(city.router)


    
# class CustomException(Exception):
#     def __init__(self, desc: str) -> None:
#         self.desc=desc



# @app.exception_handler(CustomException)
# async def my_custom_exception_handler(request: Request, exc: CustomException):
#     if exc.status_code == 404:
#         return JSONResponse(status_code=500,
#         content={"message": f"Error! {exc.name} "},)
#     else:
#         # Just use FastAPI's built-in handler for other errors
#         return await http_exception_handler(request, exc)



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
