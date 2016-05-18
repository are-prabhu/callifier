from user_auth import UserAuthValidation,AlertUser
from flask.ext.restful import reqparse, abort, Api, Resource
from callservice.plivocaller import CallerService


parser = reqparse.RequestParser()
parser.add_argument('orgkey', type=str)
parser.add_argument('projectid', type=str)
parser.add_argument('alertmsg', type=str)



class RequestValidator(Resource):
     def __init__(self):
          args = parser.parse_args()
	  self.org_token = args['orgkey']
	  self.proj_id = args['projectid']
	  self.alert_msg =  args['alertmsg']

     def alert_users(self,get_users,esclation_layer):
	  get_all_user = AlertUser().callmaker(get_users,1)
	  get_status ={}
          if type(get_all_user) == list:
	      for each_user in get_all_user:
	           user_all_info = UserAuthValidation.get_user_info(each_user)
                   user_phone_number = user_all_info['phone_number']
                   user_voice = user_all_info['voice']
                   user_language = user_all_info['language']
                             
                   call_status = CallerService().single_call_parameters(user_phone_number)                           
		   if call_status == False:
		        get_status[call_status]=user_phone_number
	  if len(get_status) == len(get_all_user):
		return False
	  return True
	    

     def post(self):
	  get_org_name = UserAuthValidation.validate_token(self.org_token)
	  if get_org_name != False:
 	       get_projid = UserAuthValidation.couch_get_projectid(get_org_name)
 	       if self.proj_id in get_projid:
		    get_all_user = UserAuthValidation.get_valid_user(self.proj_id) 		    

		    for each_esclation_layer in range(int(len(get_all_user) -2)):
		         alert_user = self.alert_users(get_all_user,each_esclation_layer)
			 if alert_user == True:
	                      return {"200":"happly call"}
			      break
		    if alert_user == False:
		         return {"523":"Phone unrechable"}

	       else:
		    return {"498": "Invalid project id"}

	  else:
	       return {"498":"Invalid token"}

	  return {"498":"Invalid request"}

#RequestValidator().PrimeRequestWorker("{'orgkey':'SPu3txvLC40mqInUtcrh','projectid':'testproject', 'alertmsg', 'alerter'}")
