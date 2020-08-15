import asyncio


import pytest


@pytest.mark.asyncio
async def test_server_info(event_loop, api):
    server_info = await api.get_server_info()
    assert server_info['authenticated'] == True