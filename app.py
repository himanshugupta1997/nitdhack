import flask

app = flask.Flask(__name__,static_folder='static')
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

@app.route('/')
def home():
	return flask.render_template('index.html')



@app.route('/query', methods = ['POST'])
def query():
	if flask.request.method == 'POST':
		print(flask.request.form)



if __name__ == "__main__":
	app.run(debug = True, port=5001)
