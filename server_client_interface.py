from server_controller import Controller
from flask import Flask,request,jsonify

app = Flask(__name__)


@app.route('/inbox',methods=['POST'])
def inbox():
	return jsonify(status = 'good',package='test')
