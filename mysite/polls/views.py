import sqlite3 as sl
from datetime import datetime as dt
from django.views.decorators.csrf import csrf_exempt

conn = sl.connect("test.db",check_same_thread=False)

from django.shortcuts import render
from django.http import HttpResponse
# from django.shortcuts import redirect

@csrf_exempt
def index(request):
    header = request.readline().decode()
    print(header)
    id = int(header)
    current = dt.now()
    print(current)
    conn.execute(f"UPDATE KSEB set YEAR = {current.year} where ID = {id}")
    conn.execute(f"UPDATE KSEB set MONTH = {current.month} where ID = {id}")
    conn.execute(f"UPDATE KSEB set DAY = {current.day} where ID = {id}")
    conn.execute(f"UPDATE KSEB set HOUR = {current.hour} where ID = {id}")
    conn.execute(f"UPDATE KSEB set MINUTE = {current.minute} where ID = {id}")
    conn.commit()

    return HttpResponse("Hello, world. You're at the polls index.")

