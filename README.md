#Callifier
Callifier is a hub for centralizing the flow of information throughout the incident lifecycle. Driven by IT and DevOps system data, Callifier provides a unified platform for real-time alerting.

###Prerequest
Setting up a Callifier development environment requires redis and couchdb.

* docker
* redis
* couchdb

For callifier development env docker containers are used here.

###Prepare Dev Env

Create python virtualenv

```sh
virtualenv callifier-project
cd callifier-project
mkdir src
cd src
source ../bin/activate
```

clone the callifier project

```sh 
git clone https://github.com/are-prabhu/callifier
cd callifier
```

install required pip package in virtual env
```sh
pip install -r requirement.txt
```

###Database Setups

####Redis setup

pull redis docker image, following is the command

```sh
$ docker pull prabhu/ubuntu14-04-redis-3.0.7

```

start redis container
```sh
$ docker run -it prabhu/ubuntu14-04-redis-3.0.7
```

start the redis process with below command. This will expose 6379 port with password as 'password'
```sh
$ redis_start
```

use the following keys to detach from the container
```sh
Ctrl p+q
```

####Couch setup

pull couchdb docker image, following is the command

```sh
$ docker pull prabhu/ubuntu14-04-couchdb
```

start couchdb container
```sh
$ docker run -it prabhu/ubuntu14-04-couchdb
```

start couchdb process will expose port number 5984 with the username 'admin' and password 'password'
```sh
$ couchdb &
```

use the following keys to detach from the container
```sh
Ctrl p+q
```

####Change config/config.yaml

In config.yaml you need to change the couchdb host IP and redis_host IP in sub tags couchdb_host: <CouchdbIP>  and redis_host: <RedisIP>

####Create sample databases for development in couch and redis

create tokendb and organizationdb in couchdb

```sh
curl  -X GET http://admin:password@<COUCHDBIP>:5984/organizationdb
curl  -X GET http://admin:password@<COUCHDBIP>:5984/tokendb
curl  -X GET http://admin:password@<COUCHDBIP>:5984/userdb
```


