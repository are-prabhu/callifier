#!/usr/bin/env python


'''
USAGE curl -X POST -H "Content-Type: application/json" -d '{ "auth_token": "auth1", "widget": "id1", "title": "Something1"ext": "Some text", "moreinfo": "Subtitle" }' http://127.0.0.1:8080/calling/v1/unlock
'''

import json
import base64
import time
import re
import math
import os
import os.path
from utils.log import Logger
from workers.user_auth import UserAuthValidation
from flaskext.couchdbkit import CouchDBKit
from flask import Flask, jsonify, abort, make_response, request, g



app = Flask(__name__)

logging = Logger.getLogger(__file__)
'''
class PhoneApplication(object):
     def __init__(self,dbconnections=None)
'''
@app.route('/calling/v1/unlock',methods=['POST'])
@app.errorhandler(404)
def caller_unlock(**kwargs):
     print request.json

     auth_token = request.json['auth_token']
     result = UserAuthValidation.validate_token(auth_token)

     return result
         


if __name__ == '__main__':
     app.run(host="127.0.0.1",port=8080,debug=True)
     #app.run()

