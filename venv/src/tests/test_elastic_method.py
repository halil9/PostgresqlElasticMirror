import sys 
sys.path.insert(0, '../mirror')
from postgres_connect import PostgresOps
obj = PostgresOps()
obj.start_listening(channel_name=sys.argv[1])
