from flask import Flask,request,jsonify
from flask_cors import CORS
from client import Client
import json

app = Flask(__name__)
CORS(app)

clients = {}


@app.route('/',methods=['POST'])
def inbox():
	
	jsonrec = json.loads(request.data.decode('utf-8'))
	
	fileDebug = open("debug.txt", "w")
	fileDebug.write(str(jsonrec))
	fileDebug.close()
	
	if jsonrec is None:
		return jsonify(status='bad')

	# Identify and process request
	if jsonrec['opperation'] == 'getMessage':
		return __get_message(jsonrec['clientID'])
	elif jsonrec['opperation'] == 'leaveMessage':
		return __leave_message(jsonrec['clientID'],jsonrec['payload'])
	elif jsonrec['opperation'] == 'newClient':
		return __new_client(None, jsonrec["payload"]["pickup"])
	elif jsonrec['opperation'] == 'delete':
		return __delete(jsonrec["clientID"])
		
	


def __new_client(cID, pickup):
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
		
		clients[cID] = Client(cID, "user")
		
		response = jsonify(status = "done", clientID = robotID, payload = {"sender": cID})
		response.headers["Access-Control-Allow-Origin"] = "*"
		response.headers["Access-Control-Allow-Credentials"] = True
		response.headers["Access-Control-Allow-Methods"] = "POST"
		response.headers["Content-Type"] = "application/json"
		
		return response
	else :		# its a robot
		clients[cID] = Client(cID, "robot")
		return jsonify(status = "done", clientID = cID)


def __leave_message(clientID,msg):
	clients[clientID].leave_message(msg)
	return jsonify(status='done')


def __get_message(clientID):
	try:
		return jsonify(status='done',payload=clients[clientID].next_message())
	except:
		return jsonify(status='bad')


def __delete(clientID) :
	try:
		del clients[clientID]
		return jsonify(status = "done")
	except:
		return jsonify(status = "bad")
