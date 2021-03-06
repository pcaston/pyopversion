"""pyopversion package."""
import asyncio

import async_timeout

from .base import OpVersionBase
from .consts import (
    DATA_CURRENT_VERSION,
    DATA_RELEASE_DATE,
    DATA_RELEASE_DESCRIPTION,
    DATA_RELEASE_NOTES,
    DATA_RELEASE_TITLE,
    DEFAULT_HEADERS,
)
from .exceptions import OpVersionInputException

URL = "https://openpeerpower.io/version.json"


class OpVersionOpio(OpVersionBase):
    """Handle versions for the openpeerpower.io source."""

    def validate_input(self) -> None:
        """Raise OpVersionInputException if expected input are missing."""
        if self.session is None:
            raise OpVersionInputException("Missing aiohttp.ClientSession")

    async def fetch(self):
        """Logic to fetch new version data."""
        async with async_timeout.timeout(self.timeout, loop=asyncio.get_running_loop()):
            request = await self.session.get(url=URL, headers=DEFAULT_HEADERS)
            self._data = await request.json()

    def parse(self):
        """Logic to parse new version data."""
        self._version = self.data.get(DATA_CURRENT_VERSION)
        self._version_data = {
            DATA_RELEASE_DATE: self.data.get(DATA_RELEASE_DATE),
            DATA_RELEASE_NOTES: self.data.get(DATA_RELEASE_NOTES),
            DATA_RELEASE_TITLE: self.data.get(DATA_RELEASE_TITLE),
            DATA_RELEASE_DESCRIPTION: self.data.get(DATA_RELEASE_DESCRIPTION),
        }
