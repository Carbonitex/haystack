from typing import Any, Callable, Coroutine
from fastapi import Response, Request
from rest_api.config import TOKEN_CRED
import logging

logging.getLogger("haystack").setLevel("INFO")
logger = logging.getLogger("haystack")

async def auth_middleware(request: Request, call_next: Callable, some_attribute: Any) -> Response:
    request.state.attr = some_attribute  # Do what you need with your attribute
    content_type = request.headers.get('Content-Type')
    logger.info(content_type)
    logger.info("test2")
    token_auth = request.headers.get('Token-Auth')
    logger.info(token_auth)
    logger.info("test")
    logger.info(TOKEN_CRED)
    logger.info("test3")
    return await call_next(request)