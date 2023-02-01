from flask import Flask, request
from datetime import datetime
import time
import pandas as pd
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
			"receiver": request.form["r"],
			"sender": request.form["s"],
			"amount": request.form["amount"],
			"time": request.form["t"],
		}
		transactions.append(transaction)
		return "Vous avez ajoutez " + str(transaction) + " à vos transactions !"
	return "Vous n'avez rien ajoutez pour l'instant !"


#E2 Afficher une liste de toutes les transactions dans l’ordre chronologique
@app.route('/transactions', methods=['GET'])
def get_transaction():
	if request.method == 'GET':
		def extract_date(d):
		            return datetime.strptime(d['time'], '%d/%m/%Y')
		sorted_transactions = sorted(transactions, key=extract_date)
		return sorted_transactions

#E3 Afficher une liste des transactions dans l’ordre chronologique liées à une personne.
@app.route('/transactions/<person>', methods=['GET'])
def get_person_transactions(person):
	if request.method == 'GET':
		person_transactions = [t for t in transactions if t['receiver'] == person or t['sender'] == person]
		def extract_date(d):
			return datetime.strptime(d['time'], '%d/%m/%Y')
		sorted_transactions = sorted(person_transactions, key=extract_date)
		return sorted_transactions

#E4 Afficher le solde du compte de la personne.
@app.route('/balance/<person>', methods=['GET'])
def get_balance(person):
    if request.method == 'GET':
        person_transactions = [t for t in transactions if t['receiver'] == person or t['sender'] == person]
        balance = 0
        for t in person_transactions:
            if t['receiver'] == person:
                balance += int(t['amount'])
            if t['sender'] == person:
                balance -= int(t['amount'])
        return str(balance)

#E5 Importer des données depuis un fichier csv (Ne marche pas)
@app.route("/import", methods=['GET'])
def load_transactions():
    transactions_df = pd.read_csv('transactions.csv')
    transactions = transactions_df.to_dict('records')
    return transactions

if __name__ == '__main__':
    app.run(debug=True)
