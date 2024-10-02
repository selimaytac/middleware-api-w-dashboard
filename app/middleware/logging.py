from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from app.core.logger import logger

class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        client_host = request.client.host
        client_port = request.client.port
        logger.info(f"Received request: {request.method} {request.url} from {client_host}:{client_port}")
        response = await call_next(request)
        logger.info(f"Response status code: {response.status_code}")
        return response
