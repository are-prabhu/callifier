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

