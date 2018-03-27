import psycopg2
import psycopg2.extensions
import json,select,datetime
from config import config
from elastic import mirror_to_elastic
class PostgresOps:
    def __init__(self):
        self.conn = psycopg2.connect(dbname="{}".format(config['db']), user="{}".format(config['username']),password="{}".format(config['passwd']))
        self.conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
        self.curs = self.conn.cursor()


    def start_listening(self,channel_name):
        self.curs.execute("LISTEN pricesinserted;")

        seconds_passed = 0
        print "Waiting for notifications on channel 'pricesinserted'"
        while 1:
            self.conn.commit()
            if select.select([self.conn],[],[],5) == ([],[],[]):
                seconds_passed += 5
                print "{} seconds passed without a notification...".format(seconds_passed)
            else:
                seconds_passed = 0
                self.conn.poll()
                self.conn.commit()
                while self.conn.notifies:
                    notify = self.conn.notifies.pop()
                    print "Got NOTIFY:", datetime.datetime.now(), notify.pid, notify.channel, notify.payload
                    mirror_to_elastic(db_name=config['db'],table_name=config['username'],data=notify.payload)

