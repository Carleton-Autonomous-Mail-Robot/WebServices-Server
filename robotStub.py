import requests
import json
import time


class RobotStub:
	def stub () :
		# Register client on server
		msg = {
			"status": "good",
			"clientID": "",
			"opperation": "newClient",
			"payload": {
				"sender": "",
				"receiver": "",
				"pickup": "",
				"destination": "",
				"currentLocation": ""},}
		
		response = requests.post("http://localhost:5000", msg)
		rID = response.json()["clientID"]
		print (response.json())
		
		# Loop getmessage on robotID until there is a request
		msgget = {
			"status": "good",
			"clientID": rID,
			"opperation": "getMessage",
			"payload": {
				"sender": "",
				"receiver": "",
				"pickup": "",
				"destination": "",
				"currentLocation": ""},}
		
		print("Listening for request...")
		while (1) :
			sleep(1)
			response = requests.post("http://localhost:5000", msgget)
			if (status == "good") :
				source = response.json()["payload"]["pickup"]
				dest = response.json()["payload"]["destination"]
				cID = respone.json()["payload"]["sender"]
				print (response.json())
				break
		
		# Push a bunch of messages that simulate the currentLocation msgs of an operating robot
		msgloop = {
			"status": "good",
			"clientID": cID,
			"opperation": "leaveMessage",
			"payload": {
				"sender": rID,
				"receiver": cID,
				"pickup": source,
				"destination": dest,
				"currentLocation": source},}
		
		x = 0
		while x < 10 :
			sleep(1)
			response = requests.post("http://localhost:5000", msgloop)
			x = x+1
			
		msgfin = {
			"status": "good",
			"clientID": cID,
			"opperation": "leaveMessage",
			"payload": {
				"sender": rID,
				"receiver": cID,
				"pickup": source,
				"destination": dest,
				"currentLocation": dest},}
				
		response = requests.post("http://localhost:5000", msgfin)
		print (response.json())
		
		# Delete robot client
		msgdel = {
			"status": "good",
			"clientID": rID,
			"opperation": "delete",
			"payload": {
				"sender": rID,
				"receiver": cID,
				"pickup": source,
				"destination": dest,
				"currentLocation": dest},}
				
		response = requests.post("http://localhost:5000", msgdel)
