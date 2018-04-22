from flask import Flask, jsonify, render_template, request, redirect
from pymongo import MongoClient
from geopy import distance
from geopy.geocoders import Nominatim



max_dist = 1

client = MongoClient()
db = client.db

medicines = db.medicines
users = db.users
pharmacies = db.phar
#medicines.remove()


app = Flask(__name__)

@app.route('/',methods=['GET'])
def index():
	return render_template('index.html')

@app.route('/medicine',methods=['POST','GET'])
def preprocess():
	#print(type_of(request))
	
	if request.method=='POST':
		#print(request.json['medicine_name0'])
		

		medicine_name = request.json['medicines']
		medicine_qty = request.json['quantities']
		lat = float(request.json.get('lat',0))
		lng = float(request.json.get('lng',0))

		req = {}
		req['medicine_name'] = medicine_name
		req['medicine_qty'] = medicine_qty
		req['lat'] = lat
		req['lng'] = lng
		
		
		
		#lat = float(request.json['lat'])
		#lng = float(request.json['lng'])

		'''
		entry = {
			'medicine_name':medicine_name,
			'medicine_qty':medicine_qty
		}


		#print(entry)
		medicines.insert_one(entry)
		'''

		result = pharmacy(req)
		
		return jsonify({'Result':result}),201
	
	
def cmp_items(a, b):
    if a.count > b.count:
        return 1
    elif a.count < b.count:
        return 0
    else:
        return -1


def pharmacy(req):

	pharma = pharmacies.find()

	print(req)
	#print(list(pharma))

	if pharma.count()==0:
		return jsonify({'none':'found'})

	ans = []

	for p in pharma:
		count = 0
		#geolocator = Nominatim()
		#location = geolocator.reverse((p['lat'],p['lng']),timeout=10)
		#print(location.address)
		if distance.distance( (req['lat'],req['lng']), (p['lat'],p['lng']) ).km <= max_dist:
			for i,med in enumerate(req['medicine_name']):
				#print(med)
				r = [c for c in p['medicines'] if c['med_name'].lower()==med.lower()]
				if len(r)==0:
					continue
				else:
					r = r[0]
					if int(req['medicine_qty'][i])<=r['med_qty']:
						count += 1
		
		if count!=0:
			pp = {}
			pp['count'] = count
			pp['name'] = p['pharma_name']
			ans.append(pp)

	ans.sort(key=lambda a: a['count'])

	#print(ans)
	return ans






@app.route('/hello', methods=['GET'])
def hello():
	return 'Hello World'

if __name__ == '__main__':
	app.run(use_reloader=True)
