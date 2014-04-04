#!usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb
import sys

# using the MySQLdb wrapper to access the info from the DB

try: 
    con = mdb.connect('localhost', 'testuser', 'test623', 'testdb');
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
