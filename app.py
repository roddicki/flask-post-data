#!/usr/bin/python
#

from flask import Flask, render_template, redirect, url_for, request
app = Flask(__name__)


@app.route('/result', methods = ['POST', 'GET'])
def result():
	if request.method == 'POST':
		user_input = request.form
		check_list =  request.form.getlist('vehicle') 
		led_msg = ''

		# trigger LED / door in this code block
		if 'Car' in check_list or 'Plane' in check_list:
			# add GPIO code to trigger red LED / door here
			led_msg = ' : You are a polluter - red LED on'
		else:
			# add GPIO code to trigger green LED / door here
			led_msg = ' : Well done for only using a bike - Green LED on'

		# generate text for result page
		msg = user_input.get('user') + ' you have the following: '
		for items in check_list:
			msg += ' ' + items

		# use result.html page 
		return render_template('result.html',result = msg + led_msg)
	else:
		return render_template('result.html',result = 'nothing received')



@app.route('/')
def index():
	return render_template('hello.html')


if __name__ == '__main__':
	# app.run(debug = True)
	app.run(host="0.0.0.0")