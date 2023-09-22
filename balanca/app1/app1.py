from flask import request, Flask
import json

app1 = Flask(__name__)

@app1.route('/')
def hello_world():
	return 'Salam alikom, this is App1 :) '

if __name__ == '__main__':
	app1.run(debug=True, host='0.0.0.0')
