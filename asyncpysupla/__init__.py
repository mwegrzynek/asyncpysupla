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
        self.base_url = 'https://{}/api/v2.3.0/'.format(server)
        self.personal_access_token = personal_access_token
        self._session = session

    def session(self):
        if self._session is None:
            self._session = aiohttp.ClientSession(
                headers={
                    'Authorization': f'Bearer {self.personal_access_token}'
                }
            )
        return self._session

    async def close(self):
        if self._session is not None:
            await self._session.close()
            self._session = None

    async def get_server_info(self):
        async with self.session().get(
            urljoin(self.base_url, 'server-info')
        ) as resp:
            return await resp.json()

    async def get_channels(self, include=None, func=None):
        params = {}

        if func is not None:
            params['function'] = ','.join(func)

        if include is not None:
            params['include'] = ','.join(include)

        async with self.session().get(
            urljoin(self.base_url, 'channels'),
            params=params
        ) as resp:
            return await resp.json()

    async def get_channel(self, channel_id, include=None):
        params = {}

        if include is not None:
            params['include'] = ','.join(include)

        async with self.session().get(
            urljoin(self.base_url, 'channels/{}'.format(channel_id)),
            params=params
        ) as resp:
            return await resp.json()

    async def execute_action(self, channel_id, action, **add_pars):
        params = dict(
            action=action
        )
        params.update(add_pars)

        async with self.session().patch(
            urljoin(self.base_url, 'channels/{}'.format(channel_id)),
            json=params
        ) as resp:
            log.debug('Action "%s" response on channel "%s": %s', action, channel_id, resp.text)
            assert 200 < resp.status < 299
