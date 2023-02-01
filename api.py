from flask import Flask, request

app = Flask(__name__)

transactions = dict()

#Landing page
@app.route("/", methods=['GET'])
def hello_world():
	ret = "Hello, World !"
	if request.method == 'GET':
		return ret

if __name__ == '__main__':
    app.run(debug=True)
