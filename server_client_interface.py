from flask import Flask,request,jsonify
from client import Client
import json

app = Flask(__name__)

clients = {}



@app.route('/',methods=['POST'])
def inbox():	
	if request.get_json() is None:
		return jsonify(status='bad')
	
	
	json = request.get_json()


	if json['opperation'] == 'getMessage':
		return __get_message(json['clientID'])
	elif json['opperation'] == 'leaveMessage':
		return __leave_message(json['clientID'],json['payload'])
	elif json['opperation'] == 'new':
		return __new_client(json['clientID'])
	return jsonify(status='bad')


def __new_client(clientID):
	clients[clientID] = Client(clientID)
	return jsonify(status = 'done')

def __leave_message(clientID,msg):
	clients[clientID].leave_message(msg)
	return jsonify(status='done')


def __get_message(clientID):
	try:
		return jsonify(status='good',payload=clients[clientID].next_message())
	except:
		return jsonify(status='done')
