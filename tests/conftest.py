# -*- coding: UTF-8 -*-
import pytest
import os


@pytest.fixture
def SERVER():
    return os.environ['SUPLA_SERVER']

@pytest.fixture
def PERSONAL_ACCESS_TOKEN():
    return os.environ['SUPLA_PERSONAL_ACCESS_TOKEN']

@pytest.fixture
def SHUTTER_ID():
    return int(os.environ['SUPLA_SHUTTER_ID'])

@pytest.fixture
async def api(SERVER, PERSONAL_ACCESS_TOKEN):
    from asyncpysupla import SuplaAPI

    api = SuplaAPI(
        server=SERVER,
        personal_access_token=PERSONAL_ACCESS_TOKEN
    )

    yield api

    await api.close()
