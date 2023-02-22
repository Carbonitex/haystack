from typing import Any, Callable, Coroutine
from fastapi import Response, Request
from rest_api.config import TOKEN_CRED


async def auth_middleware(request: Request, call_next: Callable, some_attribute: Any) -> Response:
    request.state.attr = some_attribute  # Do what you need with your attribute
    content_type = request.headers.get('Content-Type')
    print(content_type)
    print("test2")
    token_auth = request.headers.get('Token-Auth')
    print(token_auth)
    print("test")
    print(TOKEN_CRED)
    print("test3")
    return await call_next(request)