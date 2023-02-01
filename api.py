from flask import Flask, request
from datetime import datetime
app = Flask(__name__)

transactions = []

#Landing page
@app.route("/", methods=['GET'])
def hello_world():
	ret = "Hello, World !"
	if request.method == 'GET':
		return ret


#E1 Enregistrer une transaction
@app.route('/add_transaction/', methods=['POST','GET'])
def add_transaction():
	if request.method == 'POST':
		transaction = {
			"p1": request.form["sender"],
			"p2": request.form["receiver"],
			"time": datetime(2023,1,1).timestamp(),
			"solde": request.form["solde"],
		}
		return "Vous avez ajoutez " + str(transaction) + " à vos transactions !"
	return "Vous n'avez rien ajoutez pour l'instant !"



if __name__ == '__main__':
    app.run(debug=True)
