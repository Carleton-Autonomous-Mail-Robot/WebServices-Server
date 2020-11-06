from flask import Flask,request,jsonify
from src.client import Client
import json

app = Flask(__name__)

clients = {}



@app.route('/',methods=['POST'])
def inbox():	
	if request.get_json() is None:
		return jsonify(status='bad')
	
	
	json = request.get_json()


	if json['opperation'] == 'getMessage':
		return __getMessage(json['clientID'])
	elif json['opperation'] == 'leaveMessage':
		return __leaveMessage(json['clientID'],json['payload'])
	elif json['opperation'] == 'new':
		return __newClient(json['clientID'])
	return jsonify(status='bad')


def __newClient(clientID):
	clients[clientID] = Client(clientID)
	return jsonify(status = 'done')

def __leaveMessage(clientID,msg):
	clients[clientID].leaveMessage(msg)
	return jsonify(status='done')


def __getMessage(clientID):
	try:
		return jsonify(status='good',payload=clients[clientID].nextMessage())
	except:
		return jsonify(status='done')

if __name__ == '__main__':
	app.run(host='0.0.0.0',port='80',ssl_context='adhoc')