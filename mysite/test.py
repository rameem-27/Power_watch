from datetime import datetime
import subprocess
import sqlite3 as sq
import time
conn = sq.connect("test.db")
while True:
    cursor = conn.execute("SELECT id, place, operator, location, phone, year, month, day, hour, minute from KSEB")
    for row in cursor:
        values = row
        recievedTime = datetime(int(values[5]),int(values[6]),int(values[7]),int(values[8]),int(values[9]))
        difference  = datetime.now()-recievedTime
        diff_min = divmod(difference.seconds,60)[0]
#        print(diff_min)
        if  diff_min == 1 :
            print("Circuit failure at ",f"{values[1]} {values[3]} ", "for last",diff_min,"minutes")
        else:
            break   
    time.sleep(10)