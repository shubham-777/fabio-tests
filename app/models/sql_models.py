from sqlalchemy import BigInteger, Boolean, Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from database.mysql import Base


class Continent(Base):
    __tablename__ = "continents"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), index=True)
    population = Column(Integer)
    area = Column(Float)
    countries = relationship("Country", backref="continents")


class Country(Base):
    __tablename__ = "countries"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), index=True)
    population = Column(BigInteger)
    area = Column(Float)
    continent_id = Column(Integer,ForeignKey("continents.id", ondelete="CASCADE", onupdate="CASCADE"))
    no_of_hospitals = Column(Integer)
    no_of_national_parks = Column(Integer)
    cities = relationship("City", backref="countries")

class City(Base):
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), index=True)
    population = Column(BigInteger)
    area = Column(Float)
    country_id = Column(Integer,ForeignKey("countries.id", ondelete="CASCADE", onupdate="CASCADE"))
    no_of_roads = Column(Integer)
    no_of_trees = Column(Integer)
    
