from flask import Flask, jsonify, render_template, request, redirect
from pymongo import MongoClient


client = MongoClient()
db = client.db

medicines = db.medicines
users = db.users
medicines.remove()


app = Flask(__name__)

@app.route('/',methods=['GET'])
def index():
	return render_template('index.html')

@app.route('/medicine',methods=['POST','GET'])
def preprocess():
	#print(type_of(request))
	
	if request.method=='POST':
		'''
		medicine_name0 = request.form.get('medicine_name0', 'Abc')
		medicine_qty0 = int(request.form.get('medicine_qty0', 0))
		medicine_name1 = request.form.get('medicine_name1', None)
		medicine_qty1 = int(request.form.get('medicine_qty1', 0))
		medicine_name2 = request.form.get('medicine_name2', None)
		medicine_qty2 = int(request.form.get('medicine_qty2', 0))
		medicine_name3 = request.form.get('medicine_name3', None)
		medicine_qty3 = int(request.form.get('medicine_qty3', 0))
		medicine_name4 = request.form.get('medicine_name4', None)
		medicine_qty4 = int(request.form.get('medicine_qty4', 0))
		#print(request.form['medicine_name0'])
		

		medicine_name = []
		medicine_qty = []
		
		
		if medicine_name0 != None and medicine_qty0 != 0:
			medicine_name.append(medicine_name0)
			medicine_qty.append(medicine_qty0)
		if medicine_name1 != None and medicine_qty1 != 0:
			medicine_name.append(medicine_name1)
			medicine_qty.append(medicine_qty1)
		if medicine_name2 != None and medicine_qty2 != 0:
			medicine_name.append(medicine_name2)
			medicine_qty.append(medicine_qty2)
		if medicine_name3 != None and medicine_qty3 != 0:
			medicine_name.append(medicine_name3)
			medicine_qty.append(medicine_qty3)
		if medicine_name4 != None and medicine_qty4 != 0:
			medicine_name.append(medicine_name4)
			medicine_qty.append(medicine_qty4)
		


		lat = float(request.form['lat'])
		lng = float(request.form['lng'])
		'''

		medicine_name0 = request.json.get('medicine_name0', 'Abc')
		medicine_qty0 = int(request.json.get('medicine_qty0', 0))
		medicine_name1 = request.json.get('medicine_name1', None)
		medicine_qty1 = int(request.json.get('medicine_qty1', 0))
		medicine_name2 = request.json.get('medicine_name2', None)
		medicine_qty2 = int(request.json.get('medicine_qty2', 0))
		medicine_name3 = request.json.get('medicine_name3', None)
		medicine_qty3 = int(request.json.get('medicine_qty3', 0))
		medicine_name4 = request.json.get('medicine_name4', None)
		medicine_qty4 = int(request.json.get('medicine_qty4', 0))
		#print(request.json['medicine_name0'])
		

		medicine_name = []
		medicine_qty = []
		
		
		if medicine_name0 != None and medicine_qty0 != 0:
			medicine_name.append(medicine_name0)
			medicine_qty.append(medicine_qty0)
		if medicine_name1 != None and medicine_qty1 != 0:
			medicine_name.append(medicine_name1)
			medicine_qty.append(medicine_qty1)
		if medicine_name2 != None and medicine_qty2 != 0:
			medicine_name.append(medicine_name2)
			medicine_qty.append(medicine_qty2)
		if medicine_name3 != None and medicine_qty3 != 0:
			medicine_name.append(medicine_name3)
			medicine_qty.append(medicine_qty3)
		if medicine_name4 != None and medicine_qty4 != 0:
			medicine_name.append(medicine_name4)
			medicine_qty.append(medicine_qty4)
		


		lat = float(request.json['lat'])
		lng = float(request.json['lng'])


		entry = {
			'medicine_name':medicine_name,
			'medicine_qty':medicine_qty,
			'lat':lat,
			'lng':lng
		}

		#print(entry)
		medicines.insert_one(entry)

		
		return jsonify({'inserted':'entry'}),201
	
	

@app.route('/hello', methods=['GET'])
def hello():
	return 'Hello World'

if __name__ == '__main__':
	app.run(use_reloader=True)
