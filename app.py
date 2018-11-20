from flask import Flask, jsonify, make_response, request, abort
import os
import socket
from slackclient import SlackClient
import json
from urllib import request as urlRequest
import requests
import hashlib
import math
import string
import json

app = Flask(__name__)

@app.route("/")
def home():
	return "Hello and Welcome to Group 0's API stuff :)"

@app.route("/md5/<string>", methods=['GET'])
def md5(string):
	out1 = hashlib.md5(string.encode('utf-8')).hexdigest()
	return jsonify({'input':string, 'output':out1})


@app.route("/factorial/<string:inp>", methods=['GET']) 
def fact(inp):
	try:
   		val = int(inp)
	except ValueError:
		return make_response(jsonify({'error': '400: Invalid Input'}), 404)
	fact = math.factorial(int(inp))
	return jsonify({'input':inp, 'output':fact})	

@app.route("/fibonacci/<string:inp>", methods=['GET']) 
def fibo(inp):
	try:
		nterms = int(inp) 
	except ValueError:
		return make_response(jsonify({'error': '400: Invalid Input'}), 404)
	n1 = 0
	n2 = 1
	count = 0
	if nterms <= 0:
  		return make_response(jsonify({'error': '400: Invalid Input'}), 404)
	#elif nterms == 1:
	#	return jsonify({'input':inp, 'output':n1})
	else:
		group = []
		while n1 <= nterms:
			group.append(n1)
			nth = n1 + n2
			n1 = n2
			n2 = nth
			count += 1
		return jsonify({'input':inp, 'output':group})


@app.route("/is-prime/<string:inp>")
def isprime(inp):
	try:
   		val = int(inp)
	except ValueError:
		return make_response(jsonify({'error': '400: Invalid Input'}), 404)
	if val == 1:
		b = False
		return jsonify({'input':inp, 'output':b})
	elif val == 2:
		b = True
		return jsonify({'input':inp, 'output':b})
	else:
		for i in range(2, val):
			if(val%i) ==0:
				b = False
				return jsonify({'input':inp, 'output':b})
				break
			else:
				b = True
				return jsonify({'input':inp, 'output':b})



@app.route("/slack-alert/<string:string>", methods=['GET'])
def slackalert(string):
	post = {"text":"{0}".format(string)}

	json_post = json.dumps(post)
	req = urlRequest.Request("https://hooks.slack.com/services/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", data = json_post.encode('ascii'), headers = {'Content-Type': 'application/json'})
	urlRequest.urlopen(req)
	return jsonify({'input':string, 'output':True})

if __name__=='__main__':
    app.run(host='0.0.0.0', port=5000)

