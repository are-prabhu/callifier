from user_auth import UserAuthValidation


class RequestValidator(object):
     def __init__(self):
          pass

     def PrimeRequestWorker(self, token):
          if UserAuthValidation.validate_token(token) == "ok":
	       print " need calling process caller_process"

	  else:
		 return {"Error 498":"Invalid token"}




