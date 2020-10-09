from flask import Flask,request,jsonify

app = Flask(__name__)


@app.route('/',methods=['POST'])
def inbox():
	if request.get_json() is None:
		return jsonify(status='bad')
	
	req = request.get_json()

	if req['payload'] is 'good':
		return jsonify(status='good',msg='test')
