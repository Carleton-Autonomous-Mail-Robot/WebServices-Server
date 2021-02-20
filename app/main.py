from flask import Flask,request,jsonify
from flask_cors import CORS
from app.mail_controller import MailController
from app.scheduler import Scheduler
import json

app = Flask(__name__)
CORS(app)

mail_controller = MailController()
scheduler = Scheduler(mail_controller)

@app.route('/',methods=['POST'])
def inbox():
	# Identify and process request
	if request.json['opperation'] == 'getMessage':
		return __get_message(request.json['clientID'])
	elif request.json['opperation'] == 'leaveMessage':
		return __leave_message(request.json['clientID'],request.json['payload'])
	elif request.json['opperation'] == 'newClient':
		return __new_client(request.json['payload'])
	elif request.json['opperation'] == 'delete':
		return __delete(request.json["clientID"])
	else:
		return __returnResponse() # Returns a bad request

@app.route('/hello',methods=['GET'])
def hello():
	return "hello"
		

def __new_client(msg):
	id = mail_controller.newClient()
	scheduler.notifyNewClient(id,msg)
	return __returnResponse(status = "done", clientID = id)


def __leave_message(clientID,msg):
	
	if not scheduler.message_handler(clientID, msg):
		return __returnResponse(status='bad')
	else:
		return __returnResponse(status='done')


def __get_message(clientID):
	try:
		return __returnResponse(status='done',payload=mail_controller.getMail(clientID))
	except:
		return __returnResponse(status='bad')


def __delete(clientID):
	if scheduler.delete(clientID):
		mail_controller.deleteClient(clientID)
		return __returnResponse(status='done')
	else:
		return __returnResponse(status='bad')
		

def __returnResponse(status='bad',clientID = None, payload=None):
	response = jsonify(status = "done", clientID = clientID, payload = payload)
	response.headers["Access-Control-Allow-Origin"] = "*"
	response.headers["Access-Control-Allow-Credentials"] = True
	response.headers["Access-Control-Allow-Methods"] = "POST"
	response.headers["Content-Type"] = "application/json"

	return response

