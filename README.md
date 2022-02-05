# Sample wikipedia application

## Project stack
- mysql
- FastAPI service 

## Database schema

To store the geographical data, a database schema is created, which inclued `continents, countries & cities` as tables.
Relationship among this tables are `continents` to `countries` is one to many and `countries` to `cities` is one to many.


|`continents`    |`countries`                    |`cities`                     |
|----------------|-------------------------------|-----------------------------|
|*id*            |*id*                           |*id*                         |
|name            |name                           |name                         |
|population      |population                     |population                   |
|                |area                           |area                         |
|                |*continent_id*                 |*country_id*                 |
|                |no_of_hospitals                |no_of_roads                  |
|                |no_of_national_parks           |no_of_trees                  |

## Description.
* created a RESTful APIs in Python using FASTAPI framework to create, update, delete specific values.

### Project structure.
```
.
├── app
│   ├── __init__.py
│   ├── core
│   │   ├── configurations.py
│   │   └── data
│   │       └── config.ini
│   ├── crud
│   │   ├── __init__.py
│   │   ├── city.py
│   │   ├── continent.py
│   │   └── country.py
│   ├── database
│   │   ├── __init__.py
│   │   └── mysql.py
│   ├── main.py
│   ├── models
│   │   ├── __init__.py
│   │   └── sql_models.py
│   ├── routers
│   │   ├── __init__.py
│   │   ├── city.py
│   │   ├── continent.py
│   │   ├── country.py
│   │   └── health.py
│   └── schemas
│       ├── __init__.py
│       └── pyd_schemas.py
├── README.md
└── requirements.txt
```

### Part 1: 
- design and build database schema
- implemented basic apis for crusd operations on continents, countries and cities tables.