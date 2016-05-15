from flask import Flask
from flask.ext.restful import reqparse, abort, Api, Resource
from workers.handler import RequestValidator

app = Flask(__name__)
api = Api(app)


api.add_resource(RequestValidator, '/calling/v1')

if __name__ == '__main__':
	app.run( 
        host="0.0.0.0",
  )

'''
Example request
curl -X POST -H "Content-Type: application/json" -d '{"orgkey":"SPu3txvLC40mqInUtcrh","alertmsg":"yoo got problem","projectid":"projectid"}' http://127.0.0.1:5000/calling/v1
'''
  
