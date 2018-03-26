import psycopg2
import psycopg2.extensions
import json,select
from config import config
from elastic import mirror_to_elastic
class PostgresOps:
    def __init__(self):
        self.conn = psycopg2.connect(dbname="{}".format(config['db']), user="{}".format(config['username']),password="{}".format(config['passwd']))
        self.conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
        self.curs = self.conn.cursor()


    def start_listening(self,channel_name):
        self.curs.execute("LISTEN {}".format(channel_name))
        print "Waiting for notification {}".format(channel_name)
        while True:
            if select.select([self.conn],[],[],5) == ([],[],[]):
                pass
            else:
                self.conn.poll()
                while self.conn.notifies:
                    notify = self.conn.notifies.pop(0)
                    json_data = json.loads(notify.payload)
                    mirror_to_elastic(db_name=config['db'],table_name=channel_name,data=json_data)
                    print(json_data['salary'])



