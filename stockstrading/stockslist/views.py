from django.shortcuts import render
import requests
import ast , json, psycopg2
import urllib3
from django.db import connection,transaction
from django.http import HttpResponse
from .models import *
# Create your views here.


def RealTimeData(request, symbol = None):


    http = urllib3.PoolManager()
    r = http.request('GET', 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=MSFT&apikey=R411UPD2FS2HCJV9')

    somejson = r.data.decode('utf8').replace("'", '"')
    # data = json.loads(somejson)
    data = []
    a = ast.literal_eval(somejson)
    b = a.keys()
    b = list(b)
    ind = b.index('Time Series (Daily)')
    ind2 = b.index('Meta Data')
    c = list(a[b[ind]].keys())

    for i in range(0,len(c)):
        buff = (a[b[ind]][c[i]])
        data.append(buff)

    # conn = psycopg2.connect("dbname = stocksdb user=stocks_user password = stocks_password port=5432")
    conn = psycopg2.connect(host="localhost", database="stocksdb", user="stocks_user", password="stocks_password")
    cur = conn.cursor()
    # cur = conn.cursor()


    for d in range(0,len(c)):
        cur.execute("INSERT INTO stocksdetail (symbol, date, high, open, volume, low, close ) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                    (a[b[ind2]]['2. Symbol'],c[d],float(a[b[ind]][c[d]]['2. high']), float(a[b[ind]][c[d]]['1. open']), float(a[b[ind]][c[d]]['5. volume']),
                     float(a[b[ind]][c[d]]['3. low']), float(a[b[ind]][c[d]]['4. close'])))

    conn.commit()
    cur.close()
    conn.close()

    return HttpResponse("Success")




