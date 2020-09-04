# -*- coding: UTF-8 -*-
import logging
from urllib.parse import urljoin


import aiohttp


log = logging.getLogger(__name__)


class SuplaAPI:

    def __init__(
        self,
        server: str,
        personal_access_token: str,
        session: aiohttp.ClientSession = None,
    ):
        self.server = server
        self.base_url = f"https://{server}/api/v2.3.0/"
        self.personal_access_token = personal_access_token
        self.session = session if session else aiohttp.ClientSession()

    async def close(self):
        if self.session is not None:
            await self.session.close()
            self.session = None

    async def request(self, method: str, path: str, **kwargs) -> aiohttp.ClientResponse:
        """Make a request."""
        headers = kwargs.get("headers")

        if headers is None:
            headers = {}
        else:
            headers = dict(headers)

        headers["Authorization"] = f"Bearer {self.personal_access_token}"

        return await self.session.request(
            method, urljoin(self.base_url, path), **kwargs, headers=headers,
        )

    async def get_server_info(self):
        resp = await self.request("get", "server-info")
        return await resp.json()

    async def get_channels(self, include=None, func=None):
        params = {}

        if func is not None:
            params["function"] = ",".join(func)

        if include is not None:
            params["include"] = ",".join(include)

        resp = await self.request("get", "channels", params=params)
        return await resp.json()

    async def get_channel(self, channel_id, include=None):
        params = {}

        if include is not None:
            params["include"] = ",".join(include)

        resp = await self.request("get", f"channels/{channel_id}", params=params)
        return await resp.json()

    async def execute_action(self, channel_id, action, **add_pars):
        params = dict(
            action=action
        )
        params.update(add_pars)

        resp = await self.request("patch", f"channels/{channel_id}", json=params)
        log.debug("Action '%s' response on channel '%s': %s", action, channel_id, resp.text)
        assert 200 < resp.status < 299
