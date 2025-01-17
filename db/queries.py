CREATE_TABLE_register = """
    CREATE TABLE IF NOT EXISTS register (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fullname TEXT,
    age TEXT,
    email TEXT,
    city TEXT,
    phoTO TEXT
    )
"""

INSERT_register_query = """
    INSERT INTO register (fullname, age, email, city, photo)
    VALUES (?, ?, ?, ?, ?)
"""