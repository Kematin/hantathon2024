from fastapi import Request
from fastapi.middleware import Middleware
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware

from config import config


class CheckAuthorizationMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        auth_header = request.headers.get("Authorization")
        if request.url.path == "/api/js":
            return await call_next(request)
        if not auth_header or not auth_header.startswith("Bearer "):
            return JSONResponse(
                status_code=401,
                content={
                    "detail": "Unauthorized: Missing or invalid Authorization header."
                },
            )

        token = auth_header.split(" ")[1]

        if token != config.secret.get_secret_value():
            return JSONResponse(
                status_code=403,
                content={"detail": "Forbidden: Invalid Bearer Token."},
            )

        response = await call_next(request)
        return response


middleware = [Middleware(CheckAuthorizationMiddleware)]
