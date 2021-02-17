from flask import Flask,request,jsonify
from flask_cors import CORS
from app.scheduler import Scheduler
from app.mail_controller import MailController
import json

app = Flask(__name__)
CORS(app)

mail_controller = MailController()

@app.route('/',methods=['POST'])
def inbox():
	# Identify and process request
	if request.json['opperation'] == 'getMessage':
		return __get_message(request.json['clientID'])
	elif request.json['opperation'] == 'leaveMessage':
		return __leave_message(request.json['clientID'],request.json['payload'])
	elif request.json['opperation'] == 'newClient':
		return __new_client()
	elif request.json['opperation'] == 'delete':
		return __delete(request.json["clientID"])
	else:
		return __returnResponse() #returns a bad request

@app.route('/hello',methods=['GET'])
def hello():
	return "hello"
		
	


def __new_client():
	client = Client()
	clients[client.get_client_ID()] = client
	return __returnResponse(status = "done", clientID = client.get_client_ID())


def __leave_message(clientID,msg):
	clients[clientID].leave_message(msg)
	return __returnResponse(status='done')


def __get_message(clientID):
	try:
		return __returnResponse(status='done',payload=clients[clientID].next_message())
	except:
		return __returnResponse(status='bad')


def __returnResponse(status='bad',clientID = None, payload=None):
	response = jsonify(status = "done", clientID = clientID, payload = payload)
	response.headers["Access-Control-Allow-Origin"] = "*"
	response.headers["Access-Control-Allow-Credentials"] = True
	response.headers["Access-Control-Allow-Methods"] = "POST"
	response.headers["Content-Type"] = "application/json"

	return response

