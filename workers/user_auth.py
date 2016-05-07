#!/usr/bin/env python

import sys
from utils.redis_manager import RedisOperations
#from utils.couch_manager import CouchProperties,CouchOperations


class UserAuthValidation(self):
     def __init__(self):
          pass
     '''
     @staticmethod
     def validate_token(token):
	  token_user = RedisOperations.redis_lrange("auth_token")
	  if str(token) in token_user:
	       return True
	  else:
	       return False
			
	  return None
     '''
                       
     @staticmethod
     def couch_expire_date_validation(token):
          CouchProperties.tokendb_instance().name
	   
