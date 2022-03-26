import sqlite3


# CREATING AN SQL TABLE
def create_table():
    connection = sqlite3.connect("lite.db")
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    connection.commit()
    connection.close()


# INSERTING SQL DATA
def insert(item, quantity, price):
    connection = sqlite3.connect("lite.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO store VALUES (?, ?, ?)", (item, quantity, price))
    connection.commit()
    connection.close()

# If you leave insert function, everytime when you run the Python file, it will keep adding over and over.
# Better to comment out (#) this insert function after run it once.

# insert("Wine Glass", 16, 10)
# insert("Water Glass", 10, 5)
# insert("Coffee Cup", 13, 7.5)
# insert("Whiskey Glass", 16, 11.5)


# SELECTING SQL DATA
def view():
    connection = sqlite3.connect("lite.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM store")
    rows = cursor.fetchall()
    connection.close()
    return rows


# DELETING SQL DATA
def delete(item):
    connection = sqlite3.connect("lite.db")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM store WHERE item = ?", (item,))
    connection.commit()
    connection.close()

# delete("Wine Glass")


# UPDATING SQL DATA
def update(quantity, price, item):
    connection = sqlite3.connect("lite.db")
    cursor = connection.cursor()
    cursor.execute("UPDATE store SET quantity = ?, price = ? WHERE item = ?", (quantity, price, item))
    connection.commit()
    connection.close()

update(11, 6, "Water Glass")


# TO SEE THE OUTPUT OF OUR PYTHON FILE
print(view())