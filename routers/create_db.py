from peewee import *

db = SqliteDatabase('my_database.db')


class Users(Model):
    login = CharField()
    password = CharField()

    class Meta:
        database = db


class ProductList(Model):
    userId = ForeignKeyField(Users, backref='owner')

    class Meta:
        database = db


class Products(Model):
    productListId = ForeignKeyField(ProductList, backref='productList')
    name = CharField()
    quantity = CharField()

    class Meta:
        database = db


db.connect()
db.create_tables([Users, ProductList, Products])



#Создание элементов
userOne = Users.create(login='Kirill', password='kdjfvdlfjovwenvnejwo')
print(userOne)

