from log import Logger
logging = Logger.getLogger(__file__)
from config import ConfigManager
import time
from couchdb import Server, Session
from couchdb.design import ViewDefinition


COUCH_CONFIG="couchdb_config"
COUCH_PORT="couchdb_port"
COUCH_HOST="couchdb_host"
COUCH_USERNAME="couch_username"
COUCH_PASSWORD="couch_password"

TOKEN_DB="token_db"
ORG_DB="org_db"
SCHEDCALLERDB="schedcallerdb"



def get_couch_instance_from_couch_address(couch_config):
    username = couch_config[COUCH_USERNAME]    
    password = couch_config[COUCH_PASSWORD]
  
    host = couch_config[COUCH_HOST]
    port = couch_config[COUCH_PORT]

    couch_conn = Server('http://%s:%s' % (host,port))
    couch_conn.resource.credentials = (username,password)
    return couch_conn
	

class CouchProperties(object):
     def __init__(self):
	  config_obj = ConfigManager.get_instance()
	  self.config = config_obj.dataMap
	  self.couch_block = self.config.get(COUCH_CONFIG,{})
	  self.couch_connect = get_couch_instance_from_couch_address(self.couch_block)

     @staticmethod
     def orgdb_instance():
          return CouchProperties().couch_connect[CouchProperties().couch_block[ORG_DB]]
     
     @staticmethod
     def tokendb_instance():
	  return  CouchProperties().couch_connect[CouchProperties().couch_block[TOKEN_DB]]

     @staticmethod
     def schedcallerdb_instance():
	  return CouchProperties().couch_connect[CouchProperties().couch_block[SCHEDCALLERDB]]

     @staticmethod
     def schedsmsdb_instance():
	  return CouchProperties().couch_connect[CouchProperties().couch_block[SCHEDCALLERDB]]

class CouchOperations():
     def __init__(self):
	  pass	

     def couch_insert(self,db,insert_docs):
          db.save(insert_docs)	  

     def couch_update(self,db,rev_id,update_docs):
	  db.save(update_docs)

     def couch_get_view(self,db,get_token):
          view = ViewDefinition('%sview' % db.name, '%s' % db.name, '''function(doc) {if (doc._id == "%s") emit(doc);}''' % get_token)
	  view.sync(db)

	  for res in db.view('_design/%sview/_view/%s' %(db.name,db.name) ):
	       return {res.id:res.key}


#CouchOperations().couch_insert(CouchProperties.orgdb_instance(), {"_id":"imsudo","account_type":"premium","org_id":"SPu3txvLC40mqInUtcrh","allprojects":["testproject"]})
#CouchOperations().couch_get_view(CouchProperties.orgdb_instance(),"imsudo")
#CouchOperations().couch_get_view(CouchProperties.tokendb_instance(),"xihelt")

