import  argparse,json
from postgres_connect import PostgresOps
db_config = {}

parser = argparse.ArgumentParser()

parser.add_argument("--db", "-d",help="Database name with postgresql")
parser.add_argument("--username", "-u",help="Database user name of postgresql")
parser.add_argument("--passwd", "-p",help="Database user passwd of postgresql")

args = parser.parse_args()

for arg in vars(args):
    db_config['{}'.format(arg)] = getattr(args, arg)

with open('config.py', 'w') as outfile:
    obj = PostgresOps()
    if obj.test_connection(db=args.db,username=args.username,passwd=args.passwd) :
        outfile.write("config = "+str(db_config))
    else:
        print("Cannot Create connection")