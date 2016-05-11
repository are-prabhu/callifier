from user_auth import UserAuthValidation


class RequestValidator(object):
     def __init__(self):
          pass

     def PrimeRequestWorker(self, token):
          if UserAuthValidation.validate_token(token) == True:
	       print " need calling process caller_process"
	       acc_check = UserAuthValidation.couch_expire_date_validation(token)
	       if acc_check == False:
	            return {"Error 498":"Invalid token"}
	  else:
		 return {"Error 498":"Invalid token"}




