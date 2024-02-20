from sqlalchemy import select

from database import new_session, UserOrm
from models.models import User


class UserRepository:
    @classmethod
    async def add_user(cls, data: User) -> int:
        async with new_session() as session:
            user_dict = data.model_dump()

            user = UserOrm(**user_dict)
            session.add(user)
            await session.flush()
            await session.commit()
            return user.id

    @classmethod
    async def get_all(cls):
        async with new_session() as session:
            query = select(UserOrm)
            result = await session.execute(query)
            users_models = result.scalars().all()
            return users_models
