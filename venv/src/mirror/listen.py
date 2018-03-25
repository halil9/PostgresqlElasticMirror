import  argparse,json
from postgres_connect import PostgresOps

parser = argparse.ArgumentParser()
parser.add_argument("--cn", "-c",help="Channel name of communicate with postgresql")
args = parser.parse_args()
channel_name = args.cn

if channel_name != None or channel_name != '' :
    obj = PostgresOps()
    obj.start_listening(channel_name=channel_name)
else:
    print("Channel Param Cannot be EMPTY or None ! ")
