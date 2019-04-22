from behave import *
from decimal import *

from app.account import Account
from app.client import Client


@given('an existing client named "pierre-jean" with 100.0 EUR in his account')
def step_impl(context):
    balance = Decimal(100)
    account = Account(balance)
    name = "pierre-jean"
    context.client = Client(name, account)


@when('he withdraws 10.0 EUR from his account')
def step_impl(context):
    amount = Decimal(10)
    context.client.account.withdraw(amount)


@then('the new balance is 90.0 EUR')
def step_impl(context):
    assert context.client.account.balance == Decimal(90)
