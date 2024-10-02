# app/routers/__init__.py

from .elk import router as elk_router
from .rabbitmq import router as rabbitmq_router
from .redis import router as redis_router
# from .kafka import router as kafka_router

all_routers = [elk_router, rabbitmq_router, redis_router] 