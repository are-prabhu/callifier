from user_auth import UserAuthValidation
from flask.ext.restful import reqparse, abort, Api, Resource


parser = reqparse.RequestParser()
parser.add_argument('orgkey', type=str)
parser.add_argument('projectid', type=str)
parser.add_argument('alertmsg', type=str)



class RequestValidator(Resource):
     def post(self):
          args = parser.parse_args()
	
	  org_token = args['orgkey']
	  proj_id = args['projectid']

	  get_org_name = UserAuthValidation.validate_token(org_token)
	  if get_org_name != False:
 	       get_projid = UserAuthValidation.couch_get_projectid(get_org_name)
 	       if proj_id in get_projid:
	            return {"200":"happly call"}
	       else:
		    return {"498": "Invalid project id"}

	  else:
	       return {"498":"Invalid token"}

	  return {"498":"Invalid request"}

#RequestValidator().PrimeRequestWorker("{'orgkey':'SPu3txvLC40mqInUtcrh','projectid':'testproject', 'alertmsg', 'alerter'}")
