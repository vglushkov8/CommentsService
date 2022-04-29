from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import select, and_
from sqlalchemy.ext.asyncio import AsyncSession


Base = declarative_base()


class BaseOperation(Base):
    __abstract__ = True

    @classmethod
    async def get_by_id(cls, id_: str, session: AsyncSession):
        stmt = select(cls).where(and_(cls.id == id_))
        result = await session.execute(stmt)
        return result.scalar()

    async def update(self, session: AsyncSession, **fields):
        for field, value in fields.items():
            if value is not None and hasattr(self, field):
                setattr(self, field, value)
        await session.commit()

    @classmethod
    async def delete(cls, obj, session: AsyncSession):
        await session.delete(obj)
        await session.commit()
