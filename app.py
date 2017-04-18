import flask

app = flask.Flask(__name__,static_folder='static')
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

@app.route('/')
def home():
	return flask.render_template('index.html')


def NearbySearch(lat,lng,keyword,radius=1000):
	key="AIzaSyApuFoKxVMRQ2einlsA0rkx2S4WJjJIh34"  
	url="https://maps.googleapis.com/maps/api/place/nearbysearch/json?"
  	url+="location=%f,%f&" % (lat,lng)
  	url+="radius=%i&" % radius
  	url+="type=%s&" % keyword
  	url+="key=%s" % key
  	response=requests.get(url)
  	json_dict=response.json()
  	res=json_dict['results']
  	info_pack=[]
  
  	for x in res:
		placeid = x['place_id']
		url = "https://maps.googleapis.com/maps/api/place/details/json?placeid={}&key={}".format(placeid,key)
		r = requests.get(url).json()['result']
		info = {}
		info['name'] = r['name']
		info['lat'] = r['geometry']['location']['lat']
		info['lng'] = r['geometry']['location']['lng']
		info_pack.append(info)
  	return info_pack 


@app.route('/query', methods = ['POST'])
def query():
	if flask.request.method == 'POST':
		# lat,lang =
		lat, lang = 28,76
		data = {'locations':NearbySearch(lat,lng,'doctor')}
		print(flask.request.form['query'])

	return data



if __name__ == "__main__":
	app.run(debug = True, port=5003)
