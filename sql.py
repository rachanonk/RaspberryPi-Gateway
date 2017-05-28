#!/usr/bin/python
from datetime import datetime
import time
import MySQLdb
import sys

def StoreTemperature(value):
	name = "ESP"
        # Open database connection
        db = MySQLdb.connect("localhost","root","root","pi-gateway" )
        # prepare a cursor object using cursor() method
        cursor = db.cursor()
	
	date = time.strftime('%Y-%m-%d %H:%M:%S')
        date = datetime.strptime(date, "%Y-%m-%d %H:%M:%S")

        add_to_db = "INSERT INTO temperature (name, value, date) VALUES(%s,%s,%s)"
        cursor.execute(add_to_db,(name, value, date))

        db.commit()
        # disconnect from server
        db.close()

def StoreBrightness(value):
	name = "ESP"
        # Open database connection
        db = MySQLdb.connect("localhost","root","root","pi-gateway" )
        # prepare a cursor object using cursor() method
        cursor = db.cursor()
	
	date = time.strftime('%Y-%m-%d %H:%M:%S')
        date = datetime.strptime(date, "%Y-%m-%d %H:%M:%S")

        add_to_db = "INSERT INTO brightness (name, value, date) VALUES(%s,%s,%s)"
        cursor.execute(add_to_db,(name, value, date))

        db.commit()
        # disconnect from server
        db.close()

