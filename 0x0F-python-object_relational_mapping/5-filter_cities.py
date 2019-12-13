#!/usr/bin/python3
""" Module 5-select_states """
import MySQLdb
from sys import argv

if __name__ == '__main__':
    username = argv[1]
    password = argv[2]
    db_name = argv[3]
    name_state = argv[4].split(';')
    if len(name_state) == 1:
        name_state =  name_state[0]
        db = MySQLdb.connect(host="127.0.0.1", port=3306,  user=username, passwd=password, db=db_name)
        cur = db.cursor()
        cur.execute("SELECT cities.name FROM cities JOIN states ON states.id = cities.state_id WHERE states.name={}".format('"'+ name_state + '"'))
        lista = cur.fetchall()
        print(", ".join([i[0] for i in lista]))
