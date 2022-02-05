from sqlalchemy import BigInteger, Column, Float, ForeignKey, Integer, String, UniqueConstraint
from sqlalchemy.orm import relationship
from database.mysql import Base


class Continent(Base):
    __tablename__ = "continents"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, index=True)
    population = Column(Integer)
    area = Column(Float)

    countries = relationship("Country", back_populates="continent")


class Country(Base):
    __tablename__ = "countries"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True,  index=True)
    population = Column(BigInteger)
    area = Column(Float)
    continent_id = Column(Integer,ForeignKey("continents.id", ondelete="CASCADE", onupdate="CASCADE"))
    no_of_hospitals = Column(Integer)
    no_of_national_parks = Column(Integer)

    continent = relationship("Continent", back_populates="countries")
    cities = relationship("City", back_populates="country")

class City(Base):
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, index=True)
    population = Column(BigInteger)
    area = Column(Float)
    country_id = Column(Integer,ForeignKey("countries.id", ondelete="CASCADE", onupdate="CASCADE"))
    no_of_roads = Column(Integer)
    no_of_trees = Column(Integer)

    country = relationship("Country", back_populates="cities")
