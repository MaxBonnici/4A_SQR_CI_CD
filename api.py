from flask import Flask, request

app = Flask(__name__)

transactions = dict()

#Landing page
@app.route("/", methods=['GET'])
def hello_world():
	ret = "Hello, World !"
	if request.method == 'GET':
		return ret


#E1 Enregistrer une transaction
@app.route('/transactions/<transaction>', methods=['POST'])
def add_trans(transaction):
        ret = "Transaction"
        if request.method == 'POST':
                transactions[len(transactions)] = transaction
                return "You just had " + transaction + " to your transactions !"



if __name__ == '__main__':
    app.run(debug=True)
