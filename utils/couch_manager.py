from log import Logger
logging = Logger.getLogger(__file__)
from config import ConfigManager
import time
from couchdbkit import Server

COUCH_CONFIG="couchdb_config"
TOKEN_DB="token_db"
	

class CouchProperties(object):
     def __init__(self):
	  pass

     def get_couch_connection(self, couch_prop):
	  couch_conn = Server(uri = 'http://%s:%s' % (couch_prop['couchdb_host'],couch_prop['couchdb_port']))
	  return couch_conn
	 
     def connect_properties(self):
          config_obj = ConfigManager.get_instance()
	  self.config = config_obj.dataMap

	  self.couch_block = self.config.get(COUCH_CONFIG,{})
	  self.get_couch_connection(self.couch_block)

#class CouchOperations(CouchProperties):
#     def 
CouchProperties().connect_properties()
