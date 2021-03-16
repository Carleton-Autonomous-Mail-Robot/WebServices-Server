from flask import Flask,request,jsonify
from flask_cors import CORS
from app.mail_controller import MailController
from app.scheduler import Scheduler
import json

app = Flask(__name__)
CORS(app)

mail_controller = MailController()
scheduler = Scheduler(mail_controller)


@app.route('/hello',methods=['GET'])
def hello():
	return "hello"
		
@app.route('/newClient',methods=['GET'])
def new_client():
	if request.args.get('robot') is None:
		msg = None
	else:
		msg = 'robot'
	id = mail_controller.newClient()
	scheduler.notifyNewClient(id,msg)
	return __returnResponse(status = "done", clientID = id)

@app.route('/leaveMessage',methods=['POST'])
def leave_message():
	clientID = request.args.get('clientID')
	if not scheduler.message_handler(clientID, request.json['payload']):
		return __returnResponse(status='bad')
	else:
		return __returnResponse(status='done')

@app.route('/rawLeaveMessage',methods=['POST'])
def raw_leave_message():
	clientID = request.args.get('clientID')
	scheduler.raw_robot_msg_controller(clientID, request.json['payload']):
	return __returnResponse(status='done')


@app.route('/getMessage',methods=['GET'])
def get_message():
	try:
		return __returnResponse(status='done',payload=mail_controller.getMail(request.args.get('clientID')))
	except:
		return __returnResponse(status='bad')

@app.route('/delete',methods=['GET'])
def delete():
	clientID = request.args.get('clientID')
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

