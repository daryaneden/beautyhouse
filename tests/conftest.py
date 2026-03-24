import asyncio
import pytest

pytest_plugins = [
    'fixtures.masters.masters_service',
    'fixtures.infrastructure',
    'fixtures.beauty_services.beauty_services_service',
    'fixtures.beauty_services.beauty_services_repository',
    'fixtures.masters.master_profile_repository'
]


