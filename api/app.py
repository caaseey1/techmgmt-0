from flask import Flask, jsonify, make_response, request, abort, Response, stream_with_context
import os
import socket
from slackclient import SlackClient
from flask.cli import FlaskGroup #pip3 install flask.cli
from redis import Redis, RedisError
import json
from urllib import request as urlRequest
import requests
import hashlib
import math
import string
import json
import click

app = Flask(__name__)
r = Redis(host='localhost', port=6379, db=0, socket_connect_timeout=2, socket_timeout=2)
@click.group()
@app.route("/")
def hello():
    try:
        visits = r.incr("counter") #All this checks to see if redis is running
    except RedisError:
        visits = "<i>cannot connect to Redis, counter disabled</i>"

    html =  "<h3> Hello {name}!</h3>" \
        "<b>Hostname:</b> {hostname}<br/>" \
        "<b>Visits:</b> {visits}"
    return html.format(name=os.getenv("NAME", "world"), hostname=socket.gethostname(), visits=visits) 



@hello.command()
@click.argument('string')
@app.route('/kv-record/<string:inp>', methods=['POST'])
def store_key(inp):
    content = request.get_json(force=True)
    payload = {}
    payload['input'] = inp
    if r.exists(inp) == True:
        payload['output'] = False
        payload['error'] = 'key already exists, use PUT to override'
        return json.dumps(payload), 404, {'Content-Type': 'application/json; charset=utf-8'}
    else:
        r.set(inp, content.get('value'))
        if r.get(inp).decode('utf-8') == content.get('value'):
           payload['output'] = True
           return json.dumps(payload), {'Content-Type': 'application/json; charset=utf-8'}
        else:
            payload['output'] = False
            payload['error'] = 'unable to save key'
            return json.dumps(payload), 404, {'Content-Type': 'application/json; charset=utf-8'}
    
@hello.command()
@click.argument('string')
@app.route('/kv-record/<string:inp>', methods=['PUT'])
def update_key(inp):
    payload = {}
    content = request.get_json(force=True)
    r.set(inp, content.get('value'))
    payload['input'] = inp
    if r.get(inp).decode('utf-8') == content.get('value'):
        payload['output'] = True
        return json.dumps(payload), {'Content-Type': 'application/json; charset=utf-8'}
    else:
        payload['output'] = False
        payload['error'] = 'unable to override key'
        return json.dumps(payload), 404, {'Content-Type': 'application/json; charset=utf-8'}
    
@hello.command()
@click.argument('string')
@app.route('/kv-retrieve/<string:inp>')
def retrieve_key(inp):
    payload = {}
    payload['input'] = inp
    try:
        value = r.get(inp).decode('utf-8')
        payload['output'] = value
        return json.dumps(payload), {'Content-Type': 'application/json; charset=utf-8'}
    except AttributeError:
        payload['output'] = False
        payload['error'] = 'key does not exist'
        return json.dumps(payload), 404, {'Content-Type': 'application/json; charset=utf-8'}

@hello.command()
@click.argument('string')
@app.route("/md5/<string>", methods=['GET'])
def md5(string):
	out1 = hashlib.md5(string.encode('utf-8')).hexdigest()
	return jsonify({'input':string, 'output':out1})
	click.echo("The string" + str() + "has become" + str(out1) )

@hello.command()
@click.argument('inp')
@app.route("/factorial/<string:inp>", methods=['GET']) 
def fact(inp):
	try:
   		val = int(inp)
	except ValueError:
		return make_response(jsonify({'error': '400: Invalid Input'}), 404)
		click.echo("Whoops... Looks like there was a mistake. Please look over your input and try again.")
	fact = math.factorial(int(inp))
	return jsonify({'input':inp, 'output':fact})
	click.echo("The factorial of" + str(inp) + "is" + str(fact))	

@hello.command()
@click.argument('inp')
@app.route("/fibonacci/<string:inp>", methods=['GET']) 
def fibo(inp):
	try:
		nterms = int(inp) 
	except ValueError:
		return make_response(jsonify({'error': '400: Invalid Input'}), 404)
		click.echo("Whoops... Looks like there was a mistake. Please look over your input and try again.")
	n1 = 0
	n2 = 1
	count = 0
	if nterms <= 0:
  		return make_response(jsonify({'error': '400: Invalid Input'}), 404)
  		click.echo("Whoops... Looks like there was a mistake. Please look over your input and try again.")
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
		click.echo(str(inp)+ "creates a Fibonacci sequence of" + str(group))

@hello.command()
@click.argument('inp')
@app.route("/is-prime/<string:inp>")
def isprime(inp):
	try:
   		val = int(inp)
	except ValueError:
		return make_response(jsonify({'error': '400: Invalid Input'}), 404)
		click.echo("Whoops... Looks like there was a mistake. Please look over your input and try again.")
	if val == 1:
		b = False
		return jsonify({'input':inp, 'output':b})
		click.echo(str(inp) + str(b))
	elif val == 2:
		b = True
		return jsonify({'input':inp, 'output':b})
		click.echo(str(inp) + str(b))
	else:
		for i in range(2, val):
			if(val%i) ==0:
				b = False
				return jsonify({'input':inp, 'output':b})
				click.echo(str(inp) + str(b))
				break
			else:
				b = True
				return jsonify({'input':inp, 'output':b})
				click.echo(str(inp) + str(b))


@hello.command()
@click.argument('string')
@app.route("/slack-alert/<string:string>", methods=['GET'])
def slackalert(string):
	post = {"text":"{0}".format(string)}

	json_post = json.dumps(post)
	req = urlRequest.Request("https://hooks.slack.com/services/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", data = json_post.encode('ascii'), headers = {'Content-Type': 'application/json'})
	urlRequest.urlopen(req)
	return jsonify({'input':string, 'output':True})
	click.echo("Message is been sent to the slack channel")


if __name__=='__main__':
	app.run(host='0.0.0.0', port=5000) #debug=True


