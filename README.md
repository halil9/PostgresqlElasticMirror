# Postgresql Elastic Search Mirroring Tool 
<img width="100px" src="https://avatars0.githubusercontent.com/u/33815907?s=400&u=2a8757c5f1e6cf754ef1028f1a2442261ced6220&v=4"></img>

This is the tool for Postgresql and ElasticSearch Mirroring. In this section we will discuss the mirroring in two section . 

*	POSTGRESQL
*	ELASTICSEARCH

First you clone the repository from <a href="https://github.com/initack/PostgresqlElasticMirror">Github</a>.



```sh
    git clone https://github.com/initack/PostgresqlElasticMirror
    
    cd PostgresqlElasticMirror/venv
    
    source bin/activate ##for activate the virtualenvironment. 
```


Now run the generate_connection.py script 
inside of the <b>mirror</b> directory.

```sh
    cd mirror
    
    python generate_connection.py --dbname DATABASE_NAME --username POSTGRES_USER \
    	--passwd YOUR_ULTRA_TOP_SECRET_PASSWORD_OF_DATABASE
   
```

## DATABASE LEVEL
insert_query_notify.sh script has 2 parameter


* TABLE_NAME is First
* DATABASE_NAME is Second
```sh
    cd sql
    chmod +x insert_query_notify.sh
    ./insert_query_notify.sh TABLE_NAME DATABASE_NAME
    
```
End of the script for enable the TRIGGERS script wants to password of database


## ELASTICSEARHC LEVEL


After you authenticated, you must have config.py file inside of mirror directory.
For now, you can start the mirroring with ElasticSearch. Check the elasticsearch stat;

```sh
	lsof -i tcp:9200 ##default port of elastic search
```
If you have the response, your instance is UP! :clap::clap::clap:

After check the instance life, run the script is listen.py
```sh
	python listen.py --ch CHANNEL_NAME
```


## For Testing
```sh
	cd tests
	python test_elastic_method.py channel_name
    
```
## Problems

Not production grade ! :snake:
Not good for user interact !
TroubleShooting and more tests