import asyncio

import pytest

# Mark entire modules or classes with this asyncio marker.
# Only test coroutines will be affected.
pytestmark = pytest.mark.asyncio


async def test_example():
    await asyncio.sleep(1.0)
    assert True
