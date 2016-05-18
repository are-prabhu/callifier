#!/usr/bin/env python

import sys
from utils.redis_manager import RedisOperations
from utils.couch_manager import CouchProperties,CouchOperations
#from callservice.plivocaller import CallerService
from time import gmtime, strftime



class UserAuthValidation():
     def __init__(self):
          pass

     @staticmethod
     def validate_token(token):
	  token_user = RedisOperations().redis_get(token)
	  if token_user == None: 
	       return False
	  else:
	       return token_user

	  return False
                       
     @staticmethod
     def couch_get_projectid(token):
	  date_time = strftime("%Y-%m-%d_%H-%M", gmtime())
          couch_key_value = CouchOperations().couch_get_view(CouchProperties.orgdb_instance(),token) 
	  get_projectid = couch_key_value.values()[0]
	  get_projectid = get_projectid['allprojects']

	  if (type(get_projectid) == list) and (len(get_projectid) >= 1):
	       return get_projectid
          return False

     @staticmethod
     def get_valid_user(projid):
	  get_all_user = CouchOperations().couch_get_view(CouchProperties.projectdb_instance(),projid)
	  get_all_user = get_all_user.values()[0]
	  return get_all_user

     @staticmethod
     def get_user_info(username):
          get_user_info = CouchOperations().couch_get_view(CouchProperties.userdb_instance(),username)
	  get_user_info = get_user_info.values()[0]	
	  return get_user_info  


class AlertUser(object):
     def __init__(self):
          pass

     def callmaker(self,all_user,esclation_level):
          for each_value in all_user:
	       if "esclation%s"% esclation_level in each_value:
	            return all_user[each_value]
	        

#UserAuthValidation.couch_get_projectid("imsudo")
#UserAuthValidation.validate_token("SPu3txvLC40mqInUtcrh")

