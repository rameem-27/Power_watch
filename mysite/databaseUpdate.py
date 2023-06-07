import sqlite3 as sl

conn = sl.connect("test.db")

conn.execute("UPDATE KSEB SET DAY = 7 WHERE ID = 2 ")
conn.execute("UPDATE KSEB SET HOUR = 17 WHERE ID = 2 ")
conn.execute("UPDATE KSEB SET MINUTE = 55 WHERE ID = 2 ")

#conn.execute("UPDATE KSEB SET PHONE = 9562002845 WHERE ID = 2 ")

conn.commit()
conn.close()