import pytest
from app import create_app
from db import init_all


@pytest.fixture()
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })
    yield app


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()

def test_init(client):
    init_all()

def test_get_report(client):
    rv = client.get('/report')
    assert rv.json['gross-revenue']==0
    assert rv.json['expenses']==0
    assert rv.json['net-revenue']==0

def test_post_transactions_wrong_header(client):
    rv = client.post('/transactions',data='2020-12-01, Expense, 18.77, Fuel\n')
    assert rv.data == b'Invalid content type. Use text/csv.'

def test_post_transactions_successfully(client):
    rv = client.post('/transactions',data='2020-12-01, Expense, 18.77, Fuel\n',headers={'Content-Type':'text/csv'})
    assert rv.data == b'Data successfully added.'
    rv = client.get('/report')
    assert rv.json['gross-revenue']==0
    assert rv.json['expenses']==18.77
    assert rv.json['net-revenue']==-18.77

def test_post_transactions_wrong_entry(client):
    rv = client.post('/transactions',data='2020-12-01, Expense, wrong amount, Fuel\n',headers={'Content-Type':'text/csv'})
    assert rv.data == b"Invalid value for attribute Transaction.amount: ' wrong amount'"
    rv = client.post('/transactions',data='2020-14-01, Expense, 33, Fuel\n',headers={'Content-Type':'text/csv'})
    assert rv.data == b'month must be in 1..12'
    rv = client.post('/transactions',data='2020-12-01, Wrong Type, 33, Fuel\n',headers={'Content-Type':'text/csv'})
    assert rv.data == b'type must be of expense or income type'
    rv = client.post('/transactions',data='2020-12-01, Expense, 33, Fuel\n#what to enter',headers={'Content-Type':'text/csv'})
    assert rv.data == b'not enough values to unpack (expected 4, got 1)'


def test_post_transactions_more_entries_successfully(client):
    rv = client.post('/transactions',data='2020-07-04, Income, 40.00, 347 Woodrow\n2020-07-06, Income, 35.00, 219 Pleasant\n2020-12-12, Expense, 27.50, Repairs\n2020-07-15, Income, 25.00, Blackburn St.\n2020-07-16, Expense,12.45, Fuel\n2020-07-22, Income, 35.00, 219 Pleasant\n2020-07-22, Income, 40.00, 347 Woodrow\n2020-07-25, Expense, 14.21, Fuel\n2020-07-25, Income, 50.00, 19 Maple Dr.\n',headers={'Content-Type':'text/csv'})
    assert rv.data == b'Data successfully added.'
    rv = client.get('/report')
    assert rv.json['gross-revenue']==225.0
    assert rv.json['expenses']==72.93
    assert rv.json['net-revenue']==152.07
