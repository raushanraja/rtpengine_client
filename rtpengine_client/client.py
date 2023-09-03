from abc import abstractmethod, ABC
from collections.abc import Callable
from typing import Dict, Union
import aiohttp
import json
from aiohttp import ClientError, ClientConnectorError, ClientPayloadError, InvalidURL
import logging

log = logging.getLogger(__name__)


class Handler(ABC):
    @abstractmethod
    def error_handler(self, error: Exception):
        NotImplementedError()


class ExceptionHandler(Handler):
    def __init__(self, error_handler: Union[Callable, None] = None) -> None:
        if error_handler:
            self.error_handler = error_handler

    def __call__(self, func):
        async def decorated_fuction(*args, **kwargs):
            try:
                return await func(*args, **kwargs)
            except aiohttp.ClientError as e:
                self.error_handler(e)
        return decorated_fuction

    def error_handler(self, error: Exception):
        if isinstance(error, ClientError):
            log.error(f'ClientError: {error}')

        elif isinstance(error, ClientConnectorError):
            log.error(f'ClientConnectorError: {error}')

        elif isinstance(error, ClientPayloadError):
            log.error(f'ClientPayloadError: {error}')

        elif isinstance(error, InvalidURL):
            log.error(f'InvalidURL: {error}')

        else:
            log.error(f'Exception: {error}')


exception_handler = ExceptionHandler()


class AioHttpClient:

    def __init__(self, base_url, headers: Dict):
        self.base_url = base_url
        self.headers = headers
        self.session = aiohttp.ClientSession()

    async def close(self):
        await self.session.close()

    @exception_handler
    async def get(self):
        url = self.base_url 
        log.info(url)
        async with self.session.get(url, headers=self.headers) as response:
            return await response.text()

    @exception_handler
    async def post(self,  data=None):
        url = self.base_url 
        if data is not None:
            data = json.dumps(data)
        async with self.session.post(url, data=data, headers=self.headers) as response:
            return await response.text()
