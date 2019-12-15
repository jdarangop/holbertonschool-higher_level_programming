#!/usr/bin/python3
""" Module 0-select_states """
import MySQLdb
from sys import argv

if __name__ == '__main__':
    username = argv[1]
    password = argv[2]
    db_name = argv[3]
    name_state = argv[4]
    db = MySQLdb.connect(host="127.0.0.1", port=3306,
                         user=username, passwd=password, db=db_name)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name \
                 LIKE '{}' ORDER BY states.id".format(name_state))
    for i in cur.fetchall():
        print (i)
    cur.close()
    db.close()
