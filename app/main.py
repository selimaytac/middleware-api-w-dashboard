from fastapi import FastAPI
from app.routers import redis, rabbitmq, elk
from app.middleware.logging import LoggingMiddleware
from app.db.database import engine
from app.models import base
from app.core.logger import setup_logger
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.responses import HTMLResponse
from pathlib import Path

base.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse({"detail": exc.detail}, status_code=exc.status_code)

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return JSONResponse({"detail": exc.errors()}, status_code=422)

setup_logger()

app.include_router(redis.router)
app.include_router(rabbitmq.router)
app.include_router(elk.router)

app.add_middleware(LoggingMiddleware)

@app.get("/")
def read_root():
    return {"message": "Middleware API Status: 200 OK for root."}

@app.get("/dashboard")
def dashboard():
    html_path =  Path(__file__).parent / "pages/dashboard.html"
    return HTMLResponse(content=html_path.read_text(), status_code=200)
