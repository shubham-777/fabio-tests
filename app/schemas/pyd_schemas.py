from calendar import c
from pydantic import BaseModel


#==============================
# continent
#==============================
class Continent(BaseModel):
    name : str
    population: int
    area: float

    class Config():
        orm_mode = True

#==============================
# country
#==============================

class BaseCountry(BaseModel):
    name: str
    population: int
    area: float
    no_of_hospitals: int
    no_of_national_parks: int

class AddCountry(BaseModel):
    name: str
    population: int
    area: float
    no_of_hospitals: int
    no_of_national_parks: int
    continent_id: int

    class Config():
        orm_mode = True


class ShowCountry(BaseModel):
    name: str
    population: int
    area: float
    no_of_hospitals: int
    no_of_national_parks: int
    continent: Continent

    class Config():
        orm_mode = True

#==============================
# city
#==============================
class BaseCity(BaseModel):
    name: str
    population: int
    area: float
    no_of_roads: int
    no_of_trees: int

    class Config():
        orm_mode = True

class AddCity(BaseModel):
    name: str
    population: int
    area: float
    no_of_roads: int
    no_of_trees: int
    country_id: int

    class Config():
        orm_mode = True


class ShowCity(BaseModel):
    name: str
    population: int
    area: float
    no_of_roads: int
    no_of_trees: int
    country: ShowCountry

    class Config():
        orm_mode = True