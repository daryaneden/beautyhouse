import asyncio
import pytest

pytest_plugins = [
    'tests.fixture.masters_service',
    'tests.fixture.infrastructure'
]

# @pytest.fixture(scope="session") #f
# def event_loop():
#     loop = asyncio.new_event_loop()
#     yield loop
#     loop.close()
