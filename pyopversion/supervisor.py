"""pyopversion package."""
import asyncio

import async_timeout

from .base import OpVersionBase
from .consts import (
    DATA_AUDIO,
    DATA_BOARD,
    DATA_CLI,
    DATA_DNS,
    DATA_OPPOS,
    DATA_openpeerpower,
    DATA_IMAGE,
    DATA_MULTICAST,
    DATA_OBSERVER,
    DATA_OS,
    DATA_SUPERVISOR,
    DEFAULT_BOARD,
    DEFAULT_HEADERS,
    DEFAULT_IMAGE,
    LOGGER,
)
from .exceptions import OpVersionInputException

URL = "https://version.openpeerpower.io/{channel}.json"


class OpVersionSupervisor(OpVersionBase):
    """Handle versions for the Supervisor source."""

    def validate_input(self) -> None:
        """Raise OpVersionInputException if expected input are missing."""
        if self.session is None:
            raise OpVersionInputException("Missing aiohttp.ClientSession")
        if self.image is None:
            self.image = "default"

    async def fetch(self):
        """Logic to fetch new version data."""
        async with async_timeout.timeout(self.timeout, loop=asyncio.get_event_loop()):
            request = await self.session.get(
                url=URL.format(channel=self.channel), headers=DEFAULT_HEADERS
            )
            self._data = await request.json()

    def parse(self):
        """Logic to parse new version data."""
        if self.image != DEFAULT_IMAGE and self.image not in self.data.get(
            DATA_openpeerpower, {}
        ):
            LOGGER.warning(
                "Image '%s' not found, using default '%s'", self.image, DEFAULT_IMAGE
            )
            self.image = DEFAULT_IMAGE
        self._version = self.data.get(DATA_openpeerpower, {}).get(self.image)
        if self.board != DEFAULT_BOARD and self.board not in self.data.get(
            DATA_OPPOS, {}
        ):
            LOGGER.warning(
                "Board '%s' not found, using default '%s'", self.board, DEFAULT_BOARD
            )
            self.board = DEFAULT_BOARD
        self._version_data = {
            DATA_AUDIO: self.data.get(DATA_AUDIO),
            DATA_BOARD: self.board,
            DATA_CLI: self.data.get(DATA_CLI),
            DATA_DNS: self.data.get(DATA_DNS),
            DATA_OS: self.data.get(DATA_OPPOS, {}).get(self.board),
            DATA_IMAGE: self.image,
            DATA_MULTICAST: self.data.get(DATA_MULTICAST),
            DATA_OBSERVER: self.data.get(DATA_OBSERVER),
            DATA_SUPERVISOR: self.data.get(DATA_SUPERVISOR),
        }
