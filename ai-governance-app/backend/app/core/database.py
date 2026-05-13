from contextlib import asynccontextmanager
from neo4j import AsyncGraphDatabase, AsyncDriver
from app.core.config import settings

_driver: AsyncDriver | None = None


async def get_driver() -> AsyncDriver:
    global _driver
    if _driver is None:
        _driver = AsyncGraphDatabase.driver(
            settings.neo4j_uri,
            auth=(settings.neo4j_user, settings.neo4j_password),
        )
    return _driver


async def close_driver():
    global _driver
    if _driver:
        await _driver.close()
        _driver = None


async def get_session():
    driver = await get_driver()
    async with driver.session() as session:
        yield session
