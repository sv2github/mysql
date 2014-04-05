#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb

con = mdb.connect('localhost', 'testuser', 'test623', 'testdb');

with con:
   # With the 'with' keyword, the Python interpreter automatically releases the resources.
   # It also provides error handling
    
   # Variations of cursors
    cur = con.cursor()
   # cur = con.cursor(mdb.cursors.DictCursor)
    
    cur.execute("DROP TABLE IF EXISTS Writers")
    cur.execute("CREATE TABLE Writers(Id INT PRIMARY KEY AUTO_INCREMENT,\
                Name VARCHAR(25))")
    cur.execute("INSERT INTO Writers(Name) VALUES('Jack London')")
    cur.execute("INSERT INTO Writers(Name) VALUES('Honore de Balzac')")
    cur.execute("INSERT INTO Writers(Name) VALUES('Lion Feuchtwanger')")
    cur.execute("INSERT INTO Writers(Name) VALUES('Emile Zola')")
    cur.execute("INSERT INTO Writers(Name) VALUE('Truman Capote')")
    
   # Retrieving data
   # cur.execute("SELECT * FROM Writers LIMIT 5")

   # Prepared statements - using place holders instead of directly writing values
    cur.execute("UPDATE Writers SET Name = %s WHERE Id = %s", ("Guy de Maupasant", "4"))

   # To fetch all at a time
   # rows = cur.fetchall()
   # for row in rows:
   #    print row

   # To fetch one row at a time
   # for i in range(cur.rowcount):
   #     row = cur.fetchone()
   #     print row[0], row[1]

   # The dictionary cursor - There are multiple cursor types in MySQLdb module. 
   # The default cursor returns the data in a tuple of tuples. When we use a 
   # dictionary cursor, the data is sent in a form of Python Dictionaries.
   # This way we can refer to the data by their column names.

   # rows = cur.fetchall()
   # for row in rows:
   #     print row['Id'], row['Name']

   # Column Headers - Print Column Headers with the data from the table
   # rows = cur.fetchall()
   # desc = cur.description
   # print "%s %3s" %(desc[0][0], desc[1][0])

   # for row in rows:
   #     print "%2s %3s" %row
    
    print "Number of rows updated:", cur.rowcount 
