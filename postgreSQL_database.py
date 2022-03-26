import psycopg2


# CREATING AN SQL TABLE
def create_table():
    connection = psycopg2.connect("dbname = 'database1' user = '...' password = '...' host = '...' port = '...'")
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    connection.commit()
    connection.close()

create_table()


# INSERTING SQL DATA
def insert(item, quantity, price):
    connection = psycopg2.connect("dbname = 'database1' user = '...' password = '...' host = '...' port = '...'")
    cursor = connection.cursor()
    # cursor.execute("INSERT INTO store VALUES ('%s', '%s', '%s')" % (item, quantity, price))
    cursor.execute("INSERT INTO store VALUES (%s, %s, %s)", (item, quantity, price))
    connection.commit()
    connection.close()

# If you leave insert function, everytime when you run the Python file, it will keep adding over and over.
# Better to comment out (#) this insert function after run it once.

# insert("Apple", 10, 15)
# insert("Orange", 16, 13)
# insert("Kiwi", 8, 18)
# insert("Banana", 18, 10)
# insert("Strawberry", 9, 20)


# SELECTING SQL DATA
def view():
    connection = psycopg2.connect("dbname = 'database1' user = '...' password = '...' host = '...' port = '...'")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM store")
    rows = cursor.fetchall()
    connection.close()
    return rows


# DELETING SQL DATA
def delete(item):
    connection = psycopg2.connect("dbname = 'database1' user = '...' password = '...' host = '...' port = '...'")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM store WHERE item = %s", (item,))
    connection.commit()
    connection.close()

# delete("Orange")


# UPDATING SQL DATA
def update(quantity, price, item):
    connection = psycopg2.connect("dbname = 'database1' user = '...' password = '...' host = '...' port = '...'")
    cursor = connection.cursor()
    cursor.execute("UPDATE store SET quantity = %s, price = %s WHERE item = %s", (quantity, price, item))
    connection.commit()
    connection.close()

# update(18, 6.99, "Kiwi")
# update(24, 3.49, "Apple")
# update(20, 0.89, "Banana")
# update(13, 5.99, "Strawberry")

# TO SEE THE OUTPUT OF OUR PYTHON FILE
print(view())