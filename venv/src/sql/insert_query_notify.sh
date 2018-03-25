#!/bin/bash

TABLE_NAME=$1
DB_NAME=$2
FILE_NAME="$2_$1_INSERT.sql"

sed -i  -e "s/notify_CHANNEL_NAME/notify_$DB_NAME/g" test.sql 
cat test.sql-e > "$FILE_NAME"
sed -i -e "s/TABLE_NAME/$TABLE_NAME/g" "$FILE_NAME" 
rm *.sql-e


psql -d bugun_ne_yapsam_api_development -c "$(cat $FILE_NAME)"