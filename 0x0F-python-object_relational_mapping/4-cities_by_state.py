#!/usr/bin/python3
""" Module 3-select_states """
import MySQLdb
from sys import argv

if __name__ == '__main__':
    username = argv[1]
    password = argv[2]
    db_name = argv[3]
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=db_name)
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, \
                 states.name FROM cities JOIN states ON \
                 states.id = cities.state_id ORDER BY cities.id")
    for i in cur.fetchall():
        print (i)
    cur.close()
    db.close()
