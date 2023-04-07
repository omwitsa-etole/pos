from flask import Flask, render_template, request, redirect, url_for, session, abort, flash,Response
import random
import json
import time

app = Flask(__name__)
app.debug = True
app.secret_key = 'app@Server'

@app.errorhandler(404)
def page_not_found(e):
    return render_template('error-404.html'), 404

@app.errorhandler(500)
def server_error(e):
    return render_template('error-500.html'), 500

@app.route("/api/v1/<get>")
def API(get):
	response = {"success": False}
	if get == "getEmployees":
		response = {"success":True,"count": 4,"data": [{"name": "trial","department": "trialD"},{"name": "trial2","department": "trialD"}]}
	return response

@app.route("/")
def main():
	return redirect("/index.html")
@app.route("/<page>")
@app.route("/<page>/")
def pageRedirect(page):
	
	profile = request.args.get("profile")
	query = request.args.get("q")
	try:
		return render_template(page,**locals())
	except:
		abort(404)


app.run("0.0.0.0")