from dotenv import load_dotenv
from peewee import *

import os

load_dotenv()

database = MySQLDatabase(
    os.getenv("MYSQL_DATABASE"),
    user=os.getenv("MYSQL_USER"),
    passwd=os.getenv("MYSQL_PASSWORD"),
    host=os.getenv("MYSQL_HOST"),
    port=int(os.getenv("MYSQL_PORT")),
)


class UserModel(Model):
    id = AutoField(primary_key=True)
    username = CharField(max_length=50)
    email = CharField(max_length=50)
    password = CharField(max_length=50)

    class Meta:
        database = database
        table_name = "users"

class ProducModel (Model):
    id = AutoField(primary_key=True)
    name = CharField(max_length=50)
    category = CharField(max_length=50)
    price = FloatField()
    stock = IntegerField()
    bar_code = IntegerField()

    class Meta:
        database = database
        table_name = "products"

class PcModel (Model):
    id = AutoField(primary_key=True)
    mark = CharField(max_length=50)
    model = CharField(max_length=50)
    processor = CharField(max_length=50)
    ram = IntegerField()
    storage = IntegerField()

    class Meta:
        database = database
        table_name = "pcs"

class CarModel (Model):
    id = AutoField(primary_key=True)
    mark = CharField(max_length=50)
    model = CharField(max_length=50)
    age = IntegerField()
    color = CharField(max_length=50)
    price = FloatField()

    class Meta:
        database = database
        table_name = "cars"

class BookModel (Model):
    id = AutoField(primary_key=True)
    tittle = CharField(max_length=50)
    author = CharField(max_length=50)
    age = IntegerField()
    category = CharField(max_length=50)
    isbn = IntegerField()

    class Meta:
        database = database
        table_name = "books"



