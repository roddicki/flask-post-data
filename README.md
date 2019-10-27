# flask-post-data
Basic flask app the demos POST data and can be extended with GPIO on a Raspberry Pi

## Usage
Install flask https://pypi.org/project/Flask/

Note: In it's current form this flask app can be deployed so that it is visible by other machines on the same network.

To view this flask app from another device on the same network:

1. find the *local ip* address of the machine running the flask app https://www.whatismyip.com/
2. Run flask from the project dir with

		$ python -m flask run --host=0.0.0.0

2. Access the flask app via another machine at local-ip-address:5000 eg 192.168.5.67:5000


To prevent this flask app being visible from other devices on the same network:

1. Alter app.py to:
	
		app.run(debug = True)
		# app.run(host="0.0.0.0")

2. Run flask from the project dir with 

		$ python -m flask run


## Help
Useful tutorials
tutorials

https://flask.palletsprojects.com/en/1.0.x/quickstart/

https://www.fullstackpython.com/flask.html

https://www.freecodecamp.org/news/how-to-build-a-web-application-using-flask-and-deploy-it-to-the-cloud-3551c985e492/

