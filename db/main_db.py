import sqlite3
from db import queries

db = sqlite3.connect('db/database.sqlite3')
cursor = db.cursor()

async def create_db():
    if db:
        print('База данных подключена')

    cursor.execute(queries.CREATE_TABLE_store)
    cursor.execute(queries.CREATE_TABLE_detail)

async def sql_insert_store(name,size,price,foto,productid):
    cursor.execute(queries.INSERT_store_query, (None, name,size,price,foto,productid))

    db.commit()

async def sql_insert_detail(category,info, productid):
    cursor.execute(queries.INSERT_detail_query, (None, category,info, productid))

    db.commit()


    # cursor.execute(queries.CREATE_TABLE_register)

# async def sgl_insert_registered(fullname, age, email, city, photo):
#     cursor.execute(queries.INSERT_register_query, (fullname, age, email, city, photo))
#     db.commit()
