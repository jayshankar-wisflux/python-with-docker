# Ref: https://hasura.io/blog/how-to-write-dockerfiles-for-python-web-apps-6d173842ae1d/
from flask import Flask
# the all-important app variable:
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World from Jay"

if __name__ == "__main__":
	app.config['TEMPLATES_AUTO_RELOAD'] = True
	app.run(host='0.0.0.0', debug=True, port=8080)