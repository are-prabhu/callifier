#!/usr/bin/env python

import sys
from utils.redis_manager in RedisOperations


class UserAuthValidation(self):
     def __init__(self):
          pass
     @staticmethod
     def validate_token(token):
	  token_user = RedisOperations.redis_lrange("auth_token"):
	  if str(token) in token_user:
	       return "ok"
	  else:
	       return "Fail"
			
	  return None
                               

