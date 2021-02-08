from flask import Flask,request,jsonify
from client import *
import json

app = Flask(__name__)

clients = {}


@app.route('/',methods=['POST'])
def inbox():	
	if request.get_json() is None:
		return jsonify(status='bad')
	
	json = request.get_json()
	print(json)

	# Identify and process request
	if json['opperation'] == 'getMessage':
		return __get_message(json['clientID'])
	elif json['opperation'] == 'leaveMessage':
		return __leave_message(json['clientID'],json['payload'])
	elif json['opperation'] == 'newClient':
		return __new_client(__generate_client_id(), json["payload"]["pickup"])
	elif json['opperation'] == 'delete':
		return __delete(json["clientID"])
	return jsonify(status='bad')


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
		return jsonify(status = 'done', payload = jsonify(sender=cID, receiver=robotID))
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
