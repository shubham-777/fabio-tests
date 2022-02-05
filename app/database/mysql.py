from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from core.configurations import MYSQL_DBNAME, MYSQL_HOSTNAME, MYSQL_PORT, MYSQL_UNAME, MYSQL_PASS

SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{MYSQL_UNAME}:{MYSQL_PASS}@{MYSQL_HOSTNAME}:{MYSQL_PORT}/{MYSQL_DBNAME}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()