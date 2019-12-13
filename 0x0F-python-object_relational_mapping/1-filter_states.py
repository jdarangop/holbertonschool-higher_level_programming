#!/usr/bin/python3
""" Module 0-select_states """
import MySQLdb
from sys import argv

username = argv[1]
password = argv[2]
db_name = argv[3]
db = MySQLdb.connect(host="127.0.0.1", port=3306,  user=username, passwd=password, db=db_name)
cur = db.cursor()
cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id")
for i in cur.fetchall():
    print (i)
