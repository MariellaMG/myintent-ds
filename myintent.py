import os
import requests
import json
from flask import Flask, render_template, url_for, redirect, request
app = Flask(__name__)

#http://myintent.org/discover/your/word/
@app.route('/discover/your/word/')
def main_page():	
	return render_template('template.html')



# 
# @app.route('/search', methods=['POST'])
# # Redirect to the correct URL
# def redirectToUser():
# 	if request.form['username']:
# 		return redirect(url_for('showUserGists', username=request.form['username']))
# 	else:
# 		return 'Error'

if __name__ == "__main__":
	port = int(os.environ.get('PORT', 5000))
	app.debug = True
	app.run(host='0.0.0.0', port=port)