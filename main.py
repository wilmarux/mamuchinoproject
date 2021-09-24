import pyrebase
from flask import *

config = {
    "apiKey": "AIzaSyAepQyJ8cfWMrHIm8QgIvt2-96EepUIsOc",
    "authDomain": "mytaskcontrol-940a8.firebaseapp.com",
    "databaseURL": "https://mytaskcontrol-940a8.firebaseio.com",
    "projectId": "mytaskcontrol-940a8",
    "storageBucket": "mytaskcontrol-940a8.appspot.com",
    "messagingSenderId": "337804349511"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()

app = Flask(__name__)

@app.route('/add', methods=['POST'])
def basic():
	if request.form['submit'] == 'add':

		value1 = request.form['value1']
		value2 = request.form['value2']
		value3 = request.form['value3']
		value4 = request.form['value4']
		value5 = request.form['value5']

		infoampli = {"value1": value1, "value2": value2, "value3": value3, "value4": value4, "value5": value5}
		db.push(infoampli)

		info = db.get()
		to = info.val()
		return render_template('index.html', t=to.values())
	return render_template('index.html')


@app.route('/', methods=['GET'])
def list():
	info = db.get()
	to = info.val()
	return render_template('index.html', t=to.values())

if __name__ == '__main__':
	app.run(debug=True)

