from flask_app import app
from flask import render_template

@app.route('/')
def index():
    return render_template("index.html") 

@app.route('/new')
def new():
	return render_template("just.html")
	
@app.route('/vis')
def vis():
	return render_template("vis.html")
	
@app.route('/c3')
def c3():
	return render_template("c3.html")
	
@app.route('/rick')
def rick():
	return render_template("rick.html")
	
@app.route('/high')
def high():
	return render_template("high.html")