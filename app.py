from flask import flask
import os
import socket
from slackclient import SlackClient
import json
import requests
import hashlib
import math


#https://hooks.slack.com/services/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
#payload={"text": "Test post <https://alert-system.com/alerts/1234|Click here> for details!"}


#slack_token = os.environ['xoxp-231334506688-441002778951-477816806932-7a4ad35d6541039d81b13eba2749227f']
#sc = SlackClient(slack_token)


#sc.api_call(
#  "chat.postMessage",
#  channel="C0XXXXXX",
#  text="Hello from Python! --Group 0 was successful!-- :tada:",
#  thread_ts="1476746830.000003"
#)

app = Flask(__name__)

@app.route("/")


@app.route("/md5/<string>")
def md5(uservalue1):
	hashstring = uservalue1
	out1 = print(hashlib.md5(hashstring.encode('utf-8')).hexdigest())
	return "Input Received: " + uservalue1 + "<br>MD5 Hash: " + out1


@app.route("/factorial/<int>")
def fact(uservalue2):
	fact = math.factorial(int(uservalue2))
	return "Input Received: " + str(uservalue2) + "<br> Factorial: " + fact
	

@app.route("/fibonacci/<int>")
def fibo(uservalue3):
	nterms = uservalue3
	n1 = 0
	n2 = 1
	count = 0
	if nterms <= 0:
  		print("404 Error")
	elif nterms == 1:
		return "Fibonacci up to " + str(uservalue3) + ": " 
 		print(n1)
	else:
 		return "Fibonacci up to " + str(uservalue3) + ": " 
  		while count < nterms:
    		print(n1)
    		nth = n1 + n2
    		n1 = n2
    		n2 = nth
    		count += 1
    

@app.route("/is-prime/<int>")
def isprime(uservalue4)
	num = int(uservalue4)
	for i in range(2, num):
		if(num%i) ==0:
			return "False" + str(uservalue4) + "is not a prime."
			break
	else:
		return "True" + str(uservalue4) + "is prime."



@app.route("/slack-alert/<int>")

