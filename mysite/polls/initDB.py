
import sqlite3 as sq

conn = sq.connect("test.db")
# conn.execute('''CREATE TABLE KSEB
#          (ID INT PRIMARY KEY        NOT NULL,
#          PLACE             TEXT   NOT NULL,
#          OPERATOR          TEXT   NOT NULL
#          LOCATION          TEXT   NOT NULL,
#          PHONE               INT    NOT NULL,
#          YEAR                INT    NOT NULL,
#          MONTH               INT    NOT NULL,
#          DAY                 INT    NOT NULL,
#          HOUR                INT    NOT NULL,
#          MINUTE              INT    NOT NULL
#          );
#          ''')

# print("Table created successfully")

# conn.execute("INSERT INTO KSEB (ID,PLACE,OPERATOR,LOCATION,PHONE,YEAR,MONTH,DAY,HOUR,MINUTE) \
#       VALUES (1,'Mulavoor','Favas', 'https://maps.app.goo.gl/CQg1BSGrXe3x7Jz37', 9495560545, 2023,5,18,14,34)")

# conn.execute("INSERT INTO KSEB (ID,PLACE,OPERATOR,LOCATION,PHONE,YEAR,MONTH,DAY,HOUR,MINUTE) \
#       VALUES (2, 'Paipra','Rizwana','https://goo.gl/maps/Pxj8DJ1WEvrGPoq86', 9495560545, 2023,5,18,14,40)")

# conn.execute("INSERT INTO KSEB (ID,LOCATION,PHONE,YEAR,MONTH,DAY,HOUR,MINUTE) \
#       VALUES (3, 'location3', 9495560545, 2023,5,18,14,50)")

# conn.commit()

cursor = conn.execute("SELECT id, location, phone, year, month, day, hour, minute from KSEB")

for row in cursor:
   print ("ID = ", row[0])
   print ("location = ", row[1])
   print("phone = ", row[2])
   print ("year = ", row[3])
   print ("month = ", row[4])
   print ("day = ", row[5])
   print ("hour = ", row[6])
   print ("minute = ", row[7])

# conn.execute(f"UPDATE KSEB set YEAR = 2023 where ID = 1")
# conn.commit()
conn.close()