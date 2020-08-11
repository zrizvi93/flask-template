
# __main__.py

# import os
from flask import Flask,render_template #,Response,session,redirect,url_for, escape,request,g,send_from_directory

# how you initialize the flask app
app = Flask(__name__)

# decorator to set up the routes. when you go to /home in url bar, it will route to this function
@app.route('/home')
def home():
	return render_template('index.html')

@app.route('/home/start/')
def fan():
	return render_template('next.html')

# if you name this file __main__ and you run the 
if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True, port=5000)

