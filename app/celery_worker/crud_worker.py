from celery import Celery, Task
from core import configurations as config
from database.mysql import SQLALCHEMY_DATABASE_URL, SessionLocal

app = Celery('worker',
                    broker=f'amqp://{config.MB_USERNAME}:{config.MB_PASS}@{config.MB_HOSTNAME}//',
                    backend="database",
                    include=["crud.continent", "crud.country"])



class CeleryConfig:
    database_url = f"{SQLALCHEMY_DATABASE_URL}"
    task_serializer = "pickle"
    result_serializer = "pickle"
    event_serializer = "json"
    accept_content = ["application/json", "application/x-python-serialize"]
    result_accept_content = ["application/json", "application/x-python-serialize"]

app.config_from_object(CeleryConfig)