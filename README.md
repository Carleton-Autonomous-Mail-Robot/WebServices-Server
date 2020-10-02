# WebServices-Server

**Note: The Server is far from complete, the client is currently being worked on.**

A web server which facilitates confidential communications with a client.
All communications are encrypted, server doesn't care what the payload of the message is.
The payload is passed to another system which handles it. This client server pair, is meant
to be general and inserted into any enviroment, as long as message format is respected. View
documentation JSON_FORMAT.md for more information.

## Requirements:

 - Python3.7 and up
 - PyCryptoDome
 - flask
 - Linux/Unix enviroment (Versions of Mac OS which can run Python 3.7 and up are acceptable)


 ## Installation:

To install required libraries, run the following commands in WebServices-Server directory:
    

> pip3 install -r requirements.txt

## Running:
To run the server, run the following commands in the src directory

> export FLASK_APP=server_client_interface.py

>flask run

## Todo:
 - [ ] server_controller
 - [ ] client public key persistence
 - [ ] create test cases in postman