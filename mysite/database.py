from datetime import datetime
import subprocess
import sqlite3 as sq
import time
conn = sq.connect("test.db")
while True:
   cursor = conn.execute("SELECT id, place, operator, location, phone, year, month, day, hour, minute from KSEB")
   for row in cursor:
      values = row
#    print ("ID = ", row[0])
#    print ("place = ", row[1])
#    print ("operator = ", row[2])
#    print ("location = ", row[3])
#    print ("phone =", row[4])
#    print ("year = ", row[5])
#    print ("month = ", row[6], "\n")
#    print ("day = ", row[7], "\n")
#    print ("hour = ", row[8], "\n")
#    print ("minute = ", row[9], "\n")

      recievedTime = datetime(int(values[5]),int(values[6]),int(values[7]),int(values[8]),int(values[9]))
      difference  = datetime.now()-recievedTime
      diff_min = divmod(difference.seconds,60)[0]
      if diff_min > 1:
         print(f"{values[0]}, {values[1]}, {values[2]}")
         p = subprocess.Popen(f"kdeconnect-cli --send-sms 'Circuit Failure at {values[1]}' --destination {values[3]} -n 'vivomobile' ", stdout=subprocess.PIPE, shell=True)
   time.sleep(5) 
         