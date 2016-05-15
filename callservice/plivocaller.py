from utils.log import Logger
logging = Logger.getLogger(__file__)
from utils.config import ConfigManager
import plivo

PLIVO_CONFIG = "plivo_config"
PLIVO_AUTHID = "plivo_authid"
PLIVO_AUTHTOKEN = "plivo_authtoken"
PLIVO_NUMBER = "plivo_number"
PLIVO_URL = "plivo_url"
PLIVO_ANSWERURL = "plivo_answerurl"

class CallerService(object):
     def __init__(self):
          config_obj = ConfigManager.get_instance()
          self.config = config_obj.dataMap
          self.plivo_block = self.config.get(PLIVO_CONFIG,{})
     
     def single_call_parameters(self,dest_number,source_number=None):
          call_params = {}
	  call_params['from'] = source_number
	  call_params['to'] = dest_number
	  call_params['answer_url'] = self.plivo_block[PLIVO_ANSWERURL]
          call_params['answer_method'] =  "POST"

	  if source_number == None:
		  call_params['from'] = "+919999999999"

	  plivo_call = plivo.RestAPI(self.plivo_block[PLIVO_AUTHID], self.plivo_block[PLIVO_AUTHTOKEN])
	  return plivo_call.make_call(call_params)










