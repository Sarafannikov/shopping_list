import sqlalchemy
from sqlalchemy import select, delete

from database import new_session, UserOrm, ProductListOrm, ProductOrm
from models.models import User, ListOfProducts, Product


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

    @classmethod
    async def get_user(cls, login):
        async with new_session() as session:
            query = select(UserOrm).where(UserOrm.login == login)
            result = await session.execute(query)
            try:
                product_models = result.scalars().one()
                return product_models
            except sqlalchemy.exc.NoResultFound:
                return []



class ProductListRepository:
    @classmethod
    async def add_productlist(cls, data: ListOfProducts) -> int:
        async with new_session() as session:
            productlist_dict = data.model_dump()

            productlist = ProductListOrm(**productlist_dict)
            session.add(productlist)
            await session.flush()
            await session.commit()
            return productlist.id

    @classmethod
    async def get_all(cls):
        async with new_session() as session:
            query = select(ProductListOrm)
            result = await session.execute(query)
            productlist_models = result.scalars().all()
            return productlist_models


class ProductsRepository:
    @classmethod
    async def add_product(cls, data: Product) -> int:
        async with new_session() as session:
            product_dict = data.model_dump()

            product = ProductOrm(**product_dict)
            session.add(product)
            await session.flush()
            await session.commit()
            return product.id

    @classmethod
    async def get_all(cls):
        async with new_session() as session:
            query = select(ProductOrm)
            result = await session.execute(query)
            product_models = result.scalars().all()
            return product_models

    @classmethod
    async def get_from_list(cls, id):
        async with new_session() as session:
            query = select(ProductOrm).where(ProductOrm.list_id == id)
            result = await session.execute(query)
            product_models = result.scalars().all()
            return product_models

    @classmethod
    async def delete(cls, id):
        async with new_session() as session:
            query = delete(ProductOrm).where(ProductOrm.id == id)
            result = await session.execute(query)
            await session.commit()
            return True
