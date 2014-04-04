#!usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb
import sys

# Using the MySQLdb wrapper to access the info from the DB

try: 
    con = mdb.connect('localhost', 'testuser', 'test623', 'testdb');
    # We connect to the database. The connect() method has four parameters. The first
    # parameter is the host, where the MySQL database is located. In our case it if localhost,
    # for e.g. our computer. The second parameter is the database user name. It is followed by
    # the user's account password. The final parameter is the database name.

    cur = con.cursor()
    cur.execute("SELECT VERSION()")
    ver = cur.fetchone()
    print "Database version: %s " % ver

except mdb.Error, e:
    print "Error %d: %s" % (e.args[0], e.args[1])
    sys.exit(1)

finally:
    if con:
        con.close()
