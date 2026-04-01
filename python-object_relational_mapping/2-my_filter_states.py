#!/usr/bin/python3
"""Script that filters states by user input using string format."""
import MySQLdb
import sys

if __name__ == "__main__":
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        charset="utf8"
    )
    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM states WHERE BINARY name = '{}' "
        "ORDER BY id ASC".format(sys.argv[4])
    )
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()
