from flask import Flask,request,jsonify
from flask_cors import CORS
from app.client import Client
import json

app = Flask(__name__)
CORS(app)

clients = dict()


@app.route('/',methods=['POST'])
def inbox():
	# Identify and process request
	if request.json['opperation'] == 'getMessage':
		return __get_message(request.json['clientID'])
	elif request.json['opperation'] == 'leaveMessage':
		return __leave_message(request.json['clientID'],request.json['payload'])
	elif request.json['opperation'] == 'newClient':
		return __new_client(request.json["payload"]["type"])
	elif request.json['opperation'] == 'delete':
		return __delete(request.json["clientID"])
	else:
		return __returnResponse() #returns a bad request

@app.route('/hello',methods=['GET'])
def hello():
	return "hello"
		
	


def __new_client():
	if (pickup != "") :		# if there is a listed pickup, its a request from a user
		robotID = ""
		for x in clients :
			# find a robot to service client
			try:
				if (clients[x].get_client_type() == "robot") :
					robotID = clients[x].get_client_ID()
					break
			except:
				robotID = ""
		
		clients[cID] = Client(cID)
		
		return response
	else :		# its a robot
		clients[cID] = Client(cID)
		return __returnResponse(status = "done", clientID = cID)


def __leave_message(clientID,msg):
	clients[clientID].leave_message(msg)
	return __returnResponse(status='done')


def __get_message(clientID):
	try:
		return __returnResponse(status='done',payload=clients[clientID].next_message())
	except:
		return __returnResponse(status='bad')


def __delete(clientID) :
	try:
		del clients[clientID]
		return __returnResponse(status = "done")
	except:
		return __returnResponse(status = "bad")

def __returnResponse(status='bad',clientID = None, payload=None):
	response = jsonify(status = "done", clientID = robotID, payload = {"sender": cID})
	response.headers["Access-Control-Allow-Origin"] = "*"
	response.headers["Access-Control-Allow-Credentials"] = True
	response.headers["Access-Control-Allow-Methods"] = "POST"
	response.headers["Content-Type"] = "application/json"
	
	if not (clientID is None):
		response.set_cookie('clientID',clientID)

	return response

