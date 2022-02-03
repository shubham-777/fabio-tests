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

class Country(BaseModel):
    name: str
    population: int
    area: float
    no_of_hospitals: int
    no_of_national_parks: int
    continent_id: int

    class Config():
        orm_mode = True

class City(BaseModel):
    name: str
    population: int
    area: float
    no_of_roads: int
    no_of_trees: int
    country_id: int

    class Config():
        orm_mode = True
