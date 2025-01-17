import sqlite3
from db import queries

db = sqlite3.connect('db/registred.sqlite3')
cursor = db.cursor()

async def create_db():
    if db:
        print('База данных подключена')
    cursor.execute(queries.CREATE_TABLE_register)

async def sgl_insert_registered(fullname, age, email, city, photo):
    cursor.execute(queries.INSERT_register_query, (fullname, age, email, city, photo))
    db.commit()
