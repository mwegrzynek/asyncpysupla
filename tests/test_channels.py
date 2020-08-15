'''
Channel API testing
'''
import asyncio


import pytest


@pytest.mark.asyncio
async def test_list_all_channels(api):
    channels = await api.get_channels()
    assert len(channels) > 0
    assert channels[0]['id'] > 0

@pytest.mark.asyncio
async def test_list_only_shutters(api):
    channels = await api.get_channels(func=['CONTROLLINGTHEROLLERSHUTTER'])

    assert len(channels) > 0
    for chan in channels:
        assert chan['function']['name'] == 'CONTROLLINGTHEROLLERSHUTTER'

@pytest.mark.asyncio
async def test_list_only_shutters_and_light_switches(api):
    channels = await api.get_channels(func=['CONTROLLINGTHEROLLERSHUTTER', 'LIGHTSWITCH'])

    assert len(channels) > 0
    for chan in channels:
        assert chan['function']['name'] in ('LIGHTSWITCH', 'CONTROLLINGTHEROLLERSHUTTER')

@pytest.mark.asyncio
async def test_get_shutter_info(api, SHUTTER_ID):
    shutter = await api.get_channel(SHUTTER_ID)
    assert shutter['function']['name'] == 'CONTROLLINGTHEROLLERSHUTTER'

@pytest.mark.asyncio
async def test_get_shutter_info_with_iodevice_and_state(api, SHUTTER_ID):
    shutter = await api.get_channel(SHUTTER_ID, include=('iodevice', 'state'))
    assert 'shut' in shutter['state']

@pytest.mark.asyncio
async def test_open_shutters(api, SHUTTER_ID):
    await api.execute_action(SHUTTER_ID, 'REVEAL')

@pytest.mark.asyncio
async def test_close_shutters(api, SHUTTER_ID):
    await api.execute_action(SHUTTER_ID, 'SHUT')

@pytest.mark.asyncio
async def test_get_channels_with_devices_and_state(api):
    channels = await api.get_channels(include=["iodevice", "state", "connected"])
    assert 'connected' in channels[0]['state']