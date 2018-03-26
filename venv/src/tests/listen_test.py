import select
import datetime

import psycopg2
import psycopg2.extensions

conn = psycopg2.connect(database="testopesto", user="emirozbir",password='')
#conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)

curs = conn.cursor()
curs.execute("LISTEN pricesinserted;")

seconds_passed = 0
print "Waiting for notifications on channel 'pricesinserted'"
while 1:
    conn.commit()
    if select.select([conn],[],[],5) == ([],[],[]):
        seconds_passed += 5
        print "{} seconds passed without a notification...".format(seconds_passed)
    else:
        seconds_passed = 0
        conn.poll()
        conn.commit()
        while conn.notifies:
            notify = conn.notifies.pop()
            print "Got NOTIFY:", datetime.datetime.now(), notify.pid, notify.channel, notify.payload