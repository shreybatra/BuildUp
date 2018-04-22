from flask import Flask, jsonify, render_template, request
from pymongo import MongoClient


client = MongoClient()
db = client.db

medicines = db.medicines
users = db.users


app = Flask(__name__)

@app.route('/',methods=['GET'])
def index():
	return render_template('index.html')

@app.route('/medicine',methods=['POST'])
def preprocess():
	medicine_name0 = request.json.get('medicine_name0', None)
	medicine_qty0 = request.json.get('medicine_qty0', None)
	medicine_name1 = request.json.get('medicine_name1', None)
	medicine_qty1 = request.json.get('medicine_qty1', None)
	medicine_name2 = request.json.get('medicine_name2', None)
	medicine_qty2 = request.json.get('medicine_qty2', None)
	medicine_name3 = request.json.get('medicine_name3', None)
	medicine_qty3 = request.json.get('medicine_qty3', None)
	medicine_name4 = request.json.get('medicine_name4', None)
	medicine_qty4 = request.json.get('medicine_qty4', None)

	medicine_name = []
	medicine_qty = []
	
	if medicine_name0 != None and medicine_qty0 != None:
		medicine_name.append(medicine_name0)
		medicine_qty.append(medicine_qty0)
	if medicine_name1 != None and medicine_qty1 != None:
		medicine_name.append(medicine_name0)
		medicine_qty.append(medicine_qty1)
	if medicine_name2 != None and medicine_qty2 != None:
		medicine_name.append(medicine_name0)
		medicine_qty.append(medicine_qty2)
	if medicine_name3 != None and medicine_qty3 != None:
		medicine_name.append(medicine_name0)
		medicine_qty.append(medicine_qty3)
	if medicine_name4 != None and medicine_qty4 != None:
		medicine_name.append(medicine_name4)
		medicine_qty.append(medicine_qty4)



	lat = float(request.json['lat'])
	lng = float(request.json['lng'])

	entry = {
		'medicine_name':medicine_name,
		'medicine_qty':medicine_qty,
		'lat':lat
		'lng':lng
	}

	return entry


