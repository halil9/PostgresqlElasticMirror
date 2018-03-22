import select, argparse,json
import psycopg2
import psycopg2.extensions

parser = argparse.ArgumentParser()
parser.add_argument("channel_name")
args = parser.parse_args()
channel_name = args.channel_name



conn = psycopg2.connect(dbname="testopesto", user="emirozbir", password=" ")
conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
curs = conn.cursor()
curs.execute("LISTEN pricesinserted;")


print "Waiting for notification {}".format(channel_name)
while 1:
    if select.select([conn],[],[],5) == ([],[],[]):
        pass
    else:
        conn.poll()
        while conn.notifies:
            notify = conn.notifies.pop(0)
            json_data = json.loads(notify.payload)
            print(json_data['salary'])
