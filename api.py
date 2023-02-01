from flask import Flask, request
import datetime
import time
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
			"sender": request.form["s"],
			"reicever": request.form["r"],
			"time": time.mktime(datetime.datetime.strptime(str(request.form["t"]), "%d/%m/%Y").timetuple()),
			"solde": request.form["solde"],
		}
		transactions.append(transaction)
		return "Vous avez ajoutez " + str(transaction) + " à vos transactions !"
	return "Vous n'avez rien ajoutez pour l'instant !"


#E2 Afficher une liste de toutes les transactions dans l’ordre chronologique
@app.route('/transactions', methods=['GET'])
def get_transaction():
	if request.method == 'GET':
		sorted_transactions = sorted(transactions, key=lambda d: d['time'], reverse=True)
		return sorted_transactions


if __name__ == '__main__':
    app.run(debug=True)
