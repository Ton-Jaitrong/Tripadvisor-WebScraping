import mysql.connector
conn = mysql.connector.connect(user='root', password='',host='127.0.0.1',database='python')

# INSERT
#comm = "INSERT INTO foo(bar) VALUES('example1')"
#cursor = conn.cursor()
#cursor.execute(comm)
#conn.commit()
#conn.close()

# UPDATE
# comm = "UPDATE foo SET bar='example(1)' WHERE id=1"
# cursor = conn.cursor()
# cursor.execute(comm)
# conn.commit()
# conn.close()

# SELECT
# comm = "SELECT * FROM foo"
# cursor = conn.cursor()
# cursor.execute(comm)
# data = cursor.fetchall()
# conn.commit()
# conn.close()

# for r in data:
#  print(r)

# DELETE
comm = "DELETE FROM foo WHERE id=1"
cursor = conn.cursor()
cursor.execute(comm)
conn.commit()
conn.close()