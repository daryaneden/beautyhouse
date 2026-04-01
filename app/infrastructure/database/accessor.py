from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from app.settings import Settings


engine = create_async_engine(url=Settings().db_url, future=True, echo=True, pool_pre_ping=True)

AsyncSessionFactory = async_sessionmaker(
    bind=engine,
    autoflush=False,
    expire_on_commit=False
)

async def get_db_session():
    session = AsyncSessionFactory()
    try:
        yield session
    finally:
        await session.close()