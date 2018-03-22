import select
import psycopg2
import psycopg2.extensions
conn = psycopg2.connect(dbname="testopesto", user="emirozbir", password=" ")
conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)

curs = conn.cursor()
curs.execute("LISTEN pricesinserted;")

print "Waiting for notifications on channel 'test'"
while 1:
    if select.select([conn],[],[],5) == ([],[],[]):
        print "Timeout"
    else:
        conn.poll()
        while conn.notifies:
            notify = conn.notifies.pop(0)
            print "Got NOTIFY:", notify.pid, notify.channel, notify.payload
