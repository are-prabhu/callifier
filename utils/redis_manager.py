from log import Logger
logging = Logger.getLogger(__file__)
import redis
import smhasher
from config import ConfigManager
import time

REDIS_CONFIG="redis_config"
REDIS_TOKEN_EXPIRE="redis_trial_token_expire"

def get_redis_instance_from_redis_address(redis_addr,strict_client=False, prop=None):
     if redis_addr:
          prop = dict() if prop is None else prop

          kwargs = dict()
          kwargs["host"] = redis_addr['redis_host']
	  kwargs["port"] = redis_addr['redis_port']
	  kwargs["password"] = redis_addr['redis_password']
	  kwargs["db"] = 0
          kwargs["max_connections"] = redis_addr['max_connections']
	  kwargs["socket_connect_timeout"] = redis_addr['connect_timeout']
	  redis_pool = redis.BlockingConnectionPool(**kwargs)

          if strict_client:
               return redis.StrictRedis(connection_pool=redis_pool)
          else:
               return redis.Redis(connection_pool=redis_pool)

     return None
	  

class RedisProperties(object):
     def redis_connect_properties(self):
          config_obj = ConfigManager.get_instance()
          self.config = config_obj.dataMap
     
          self.redis_block = self.config.get(REDIS_CONFIG,{})	  
          self.redis_connect = get_redis_instance_from_redis_address(self.redis_block)


class RedisOperations(RedisProperties): 
     def __init__(self):
          super(RedisOperations,self).redis_connect_properties()

     def redis_set(self,set_value,set_key):
	  self.redis_connect.set(set_value,set_key)	 

     def redis_trail_set(self,set_value,default_expire=None):
	  if default_expire == None:
	       self.redis_connect.expire(set_value,self.redis_block[REDIS_TOKEN_EXPIRE])
	  else:
               self.redis_connect.expire(set_value,default_expire)

     def redis_get(self,get_value):
	  return self.redis_connect.get(get_value)
	  
     def redis_rpush(self,push_key,push_value):
       	  if str(push_key) == "auth_token":
	       self.redis_connect.lpush("auth_token",push_value)          

	  else:
	       self.redis_connect.lpush(push_key,push_value)          

     def redis_lrange(self,range_key,range_from=None,range_to=None):
	  if range_key == "auth_token":
	       return self.redis_connect.lrange("auth_token",-1000,1000)
	  else:
	       return self.redis_connect.lraneg(range_key,range_from,range_to)


#RedisOperations().redis_set("SPu3txvLC40mqInUtcrh","imsudo")	 
#RedisOperations().redis_trail_set("auth_token",1)
#RedisOperations().redis_get("auth_token")
#RedisOperations().redis_lrange("auth_token")

