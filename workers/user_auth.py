#!/usr/bin/env python

import sys
from utils.redis_manager import RedisOperations
from utils.couch_manager import CouchProperties,CouchOperations
from time import gmtime, strftime



class UserAuthValidation():
     def __init__(self):
          pass

     @staticmethod
     def validate_token(token):
	  token_user = RedisOperations.redis_lrange("auth_token")
	  print token_user
	  if str(token) in token_user:
	       return True
	  else:
	       return False
			
	  return None
                       
     @staticmethod
     def couch_expire_date_validation(token):
	  date_time = strftime("%Y-%m-%d_%H-%M", gmtime())
          couch_key_value = CouchOperations().couch_get_view(CouchProperties.tokendb_instance(),token) 

	  if type(couch_key_value) == dict:
	       all_values = couch_key_value.values()[0]

	       if (str(all_values['account_type']) != "premium") and (all_values['account_expires'] == str(date_time)):
		    print "need to call"	             
               else:
                    return False
                    	            	             

#UserAuthValidation.couch_expire_date_validation("testtoken")
#UserAuthValidation.validate_token("testtoken")


