#!/usr/bin/python3
''' script that lists all states from the database hbtn_0e_0_usa'''
if __name__ == "__main__":
    import mySQLdb
    import sys

    db = MySQLdb.connect(user=sys.argv[1],
                            passwd=sys.argv[2],
                            db=sysargv[3])
    c = db.cursor()
    cur.execute("SELECT * FROM states ORDER by id ASC")
    for row in c.fetchall():
        print(row)
    c.close()
    db.close()
