import os
import time
import random
import psycopg2
from datetime import datetime


people = [
    ('James', 'sales'),
    ('Kim', 'manufacturing'),
    ('Rodney', 'sales'),
    ('William', 'engineering'),
    ('Drew', 'support')
]

def load(connection):
    cur = connection.cursor()
    insert = "INSERT into rating (name, score, division, created_at) VALUES (%s, %s, %s, %s);"
    for rec in people:
        cur.execute(insert, (rec[0], random.randint(0, 100), rec[1], datetime.now()))

    cur.execute("select * from rating;")
    for row in cur:
        print("result: {}".format(row))
    cur.close()

if __name__ == "__main__":
    dbname = os.environ.get('USER_DB', None)
    dbuser = os.environ.get('USER_NAME', None)
    dbpass = os.environ.get('USER_PASSWORD', None)
    dbhost = os.environ.get('DB_HOST', None)
    print("Loading database '{}' as user:{}@{}....".format(dbname, dbuser, dbhost))

    for x in range(0, 5):
        try:
            connection = psycopg2.connect(dbname=dbname, user=dbuser, password=dbpass, host=dbhost)
        except Exception:
            print("Connection failed, retry in a second")
            time.sleep(1)

    load(connection)
    connection.close()
