import psycopg2
import psycopg2.extensions
import json,select
from config import config
class PostgresOps:
    def __init__(self):
        self.conn = psycopg2.connect(dbname="{}".format(config['db']), user="{}".format(config['username']),password="{}".format(config['passwd']))
        self.conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
        self.curs = self.conn.cursor()


    def start_listening(self,channel_name):
        self.curs.execute("LISTEN {}".format(channel_name))
        print "Waiting for notification {}".format(channel_name)
        while 1:
            if select.select([self.conn],[],[],5) == ([],[],[]):
                pass
            else:
                self.conn.poll()
                while self.conn.notifies:
                    notify = self.conn.notifies.pop(0)
                    json_data = json.loads(notify.payload)
                    print(json_data['salary'])

    def test_connection(self,db,username,passwd):
        try:
            conn = psycopg2.connect(dbname=db, user=username,password=passwd)
        except Exception as exp:
            print(exp)
