import  argparse, json, psycopg2

def test_connection(db,username,passwd):
    try:
        conn = psycopg2.connect(dbname=db, user=username,password=passwd)
        return True
    except Exception as exp:
        print(exp)

db_config = {}

parser = argparse.ArgumentParser()

parser.add_argument("--db", "-d",help="Database name with postgresql")
parser.add_argument("--username", "-u",help="Database user name of postgresql")
parser.add_argument("--passwd", "-p",help="Database user passwd of postgresql")

args = parser.parse_args()
print(args)
for arg in vars(args):
    db_config['{}'.format(arg)] = getattr(args, arg)

if test_connection(db=args.db,username=args.username,passwd=args.passwd) :

    with open('config.py', 'w') as outfile:
            outfile.write("config = "+str(db_config))
else:
    print("Cannot Create connection")

