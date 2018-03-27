import select
import datetime

import psycopg2
import psycopg2.extensions

conn = psycopg2.connect(database="postgres", user="halilkrvn",password='12345')
#conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)

curs = conn.cursor()
curs.execute("LISTEN notify_asd;")

seconds_passed = 0
print "Waiting for notifications on channel 'notify_asd'"
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

