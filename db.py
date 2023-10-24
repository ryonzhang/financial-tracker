import uuid
from pony.orm import *
from datetime import datetime
from pony.orm.serialization import to_dict
database = Database()


AGGREGATE_ID='AGGREGATE'

class Transaction(database.Entity):
    id = PrimaryKey(str, auto=True)
    date = Required(datetime)
    type = Required(str)
    amount = Required(float)
    memo=Optional(str)


class Aggregrate(database.Entity):
    id = PrimaryKey(str)
    gross_revenue = Required(float)
    expenses = Required(float)
    net_revenue = Required(float)

@db_session
def create_transactions(rows):
    transactions=[]
    diff_income=0
    diff_expense=0
    for row in rows:
        uid = uuid.uuid4()
        date, type, amount, memo = row.strip().split(',')
        if type.strip() not in ['Expense','Income']:
            raise Exception('type must be of expense or income type')
        transactions.append(Transaction(id=str(uid),date=date,type=type.strip(),amount=amount,memo=memo))
        if type.strip()=='Expense':
            diff_expense+=float(amount)
        else:
            diff_income+=float(amount)
    aggregate=Aggregrate.get(id=AGGREGATE_ID)
    if aggregate is None:
        Aggregrate(id=AGGREGATE_ID,gross_revenue=diff_income,expenses=diff_expense,net_revenue=diff_income-diff_expense)
    else:
        aggregate.gross_revenue+=diff_income
        aggregate.expenses+=diff_expense
        aggregate.net_revenue+=diff_income-diff_expense
    commit()

@db_session
def get_aggregate():
    return Aggregrate.get(id=AGGREGATE_ID)

@db_session
def get_transactions():
    transactions=list(Transaction.select())
    return to_dict(transactions)

@db_session
def remove_transaction(transaction_id):
    transaction=Transaction.get(id=transaction_id)
    aggregate=get_aggregate()
    if transaction is not None:
        if transaction.type.strip()=='Expense':
            aggregate.net_revenue+=float(transaction.amount)
            aggregate.expenses-=float(transaction.amount)
        else:
            aggregate.net_revenue-=float(transaction.amount)
            aggregate.gross_revenue-=float(transaction.amount)
    transaction.delete()
    commit()

@db_session
def init_all():
    transactions=Transaction.select()
    for transaction in transactions:
        transaction.delete()
    aggregates=Aggregrate.select()
    for aggregate in aggregates:
        aggregate.delete()

@db_session
def tally_transactions():
    transactions=Transaction.select()
    income=0
    expense=0
    aggregate=get_aggregate()
    for transaction in transactions:
        if transaction.type.strip()=='Expense':
            expense+=transaction.amount
        else:
            income+=transaction.amount
    aggregate.gross_revenue=income
    aggregate.expenses=expense
    aggregate.net_revenue=income-expense
    commit()

def create_tables():
    database.generate_mapping(create_tables=True)

database.bind(provider='postgres', user='dusikfml', password='Z8HLXjtg0BfTdUTT8zqd6astUOOKwWUj', host='flora.db.elephantsql.com', database='dusikfml')

create_tables()


