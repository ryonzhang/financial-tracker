from flask import Flask, request, jsonify

from db import create_transactions, get_aggregate, get_transactions, \
    remove_transaction, tally_transactions

app = Flask(__name__)

@app.route('/transactions', methods=['POST'])
def add_transactions():
    if request.content_type == 'text/csv':
        try:
            csv_data = request.data.decode('utf-8').strip().split('\n')
            create_transactions(csv_data)
            return 'Data successfully added.', 201
        except Exception as error:
            return str(error), 500
    else:
        return 'Invalid content type. Use text/csv.', 400

@app.route('/transactions', methods=['GET'])
def obtain_transactions():
    return jsonify(get_transactions()),200

@app.route('/transactions/<transaction_id>', methods=['DELETE'])
def delete_transaction(transaction_id):
    try:
        remove_transaction(transaction_id)
        return 'delete successfully',200
    except Exception as error:
        return str(error), 500

@app.route('/tally', methods=['GET'])
def tally():
    try:
        tally_transactions()
        return 'tally successfully',200
    except Exception as error:
        return str(error), 500


@app.route('/report', methods=['GET'])
def generate_report():
    aggregate=get_aggregate()
    if aggregate is None:
        report={
            'gross-revenue': 0,
            'expenses': 0,
            'net-revenue': 0
        }
    else:
        report = {
            'gross-revenue': aggregate.gross_revenue,
            'expenses': aggregate.expenses,
            'net-revenue': aggregate.net_revenue
        }
    return jsonify(report)


def create_app():
    return app

if __name__ == '__main__':
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)
