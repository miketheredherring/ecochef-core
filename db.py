from urllib.parse import urlunparse

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from conf import (
    DATABASE_HOST, DATABASE_PASSWORD, DATABASE_USER,
    DEBUG
)


# Define module variables
engine = create_async_engine(
    'postgresql+asyncpg://%(user)s:%(password)s@%(host)s/%(database)s' % {
        'user': DATABASE_USER,
        'password': DATABASE_PASSWORD,
        'host': DATABASE_HOST,
        'database': 'main'
    },
    echo=DEBUG
)
AsyncSession = sessionmaker(engine, class_=AsyncSession)

async def build(confirm=False):
    '''Build all tables and indexes for database.
    '''
    from models import Base
    if confirm:
        async with engine.begin() as connection:
            await connection.run_sync(Base.metadata.dropall)
            await connection.run_sync(Base.metadata.create_all)

async def provision(confirm=False):
    async with engine.begin() as connection:
        await connection.execute('CREATE DATABASE main;')
        await connection.execute(
            'CREATE USER :username WITH PASSWORD \':password\';',
            {
                'username': DATABASE_USER,
                'password': DATABASE_PASSWORD
            }
        )
