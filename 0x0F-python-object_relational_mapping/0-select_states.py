#!/usr/bin/python3
'''script that lists all states from the database hbtn_0e_0_usa'''
if __name__ == "__main__":
    import mySQLdb
    import sys

    d = MySQLdb.connect(user=sys.argv[1],
                        passwd=sys.argv[2],
                        db=sys.argv[3])
    c = d.cursor()
    c.execute("SELECT * FROM states ORDER BY id ASC")
    for row in c.fetchall():
        print(row)
    c.close()
    d.close()
