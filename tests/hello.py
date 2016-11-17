import flask

app = flask.Flask(__name__)

@app.route('/')
def index():
	return "Test OK!"

if __name__ == '__main__':
	app.run(debug=False)
	index()