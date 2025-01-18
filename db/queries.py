# CREATE_TABLE_register = """
#     CREATE TABLE IF NOT EXISTS register (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     fullname TEXT,
#     age TEXT,
#     email TEXT,
#     city TEXT,
#     photo TEXT
#     )
# """
#
# INSERT_register_query = """
#     INSERT INTO register (fullname, age, email, city, photo)
#     VALUES (?, ?, ?, ?, ?)
# """

CREATE_TABLE_store = """
    CREATE TABLE IF NOT EXISTS register (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    size TEXT,
    price TEXT,
    photo TEXT,
    productid TEXT
    )
"""

INSERT_store_query = """
    INSERT INTO store 
    VALUES (?, ?, ?, ?, ?, ?)
"""

CREATE_TABLE_detail = """
    CREATE TABLE IF NOT EXISTS register (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    category TEXT,
    infoproduct TEXT,
    productid TEXT
    )
"""

INSERT_detail_query = """
    INSERT INTO detail 
    VALUES (?, ?, ?, ?)
"""