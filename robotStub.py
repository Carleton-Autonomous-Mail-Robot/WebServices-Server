import requests
import json
import time

 # DOES NOT WORK YET!!!!!

def stub () :
	# Register client on server
	msg = {
		"status": "good",
		"clientID": "",
		"opperation": "newClient",
		"payload": {
			"sender": "",
			"pickup": "",
			"destination": "",
			"currentLocation": ""},}
		
	response = requests.post("http://localhost:5000", json=msg, headers={'Content-Type': 'application/json'})
	print (response.text)
	rID = response.json()["clientID"]
	
	# Loop getmessage on robotID until there is a request
	msgget = {
		"status": "good",
		"clientID": rID,
		"opperation": "getMessage",
		"payload": {
			"sender": "",
			"pickup": "",
			"destination": "",
			"currentLocation": ""},}
		
	print("Listening for request...")
	while (1) :
		sleep(1)
		response = requests.post("http://localhost:5000", json = msgget)
		if (response["status"] == "good") :
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
			"pickup": source,
			"destination": dest,
			"currentLocation": source},}
		
	x = 0
	while x < 10 :
		sleep(1)
		response = requests.post("http://localhost:5000", json = msgloop)
		x = x+1
			
	msgfin = {
		"status": "good",
		"clientID": cID,
		"opperation": "leaveMessage",
		"payload": {
			"sender": rID,
			"pickup": source,
			"destination": dest,
			"currentLocation": dest},}
				
	response = requests.post("http://localhost:5000", json = msgfin)
	print (response.json())
		
	# Delete robot client
	msgdel = {
		"status": "good",
		"clientID": rID,
		"opperation": "delete",
		"payload": {
			"sender": rID,
			"pickup": source,
			"destination": dest,
			"currentLocation": dest},}
				
	response = requests.post("http://localhost:5000", json = msgdel)
	

if __name__ == '__main__':
	stub()
