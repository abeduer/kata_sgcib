# Kata SGCIB

## Context

- Feature: Withdraw from account
  - As a client of the bank
  - I want to withdraw money from my account
  - In order to have cash
- Scenario: An existing client withdraws from his account
  - Given an existing client named "pierre-jean" with 100.0 EUR in his account
  - When he withdraws 10.0 EUR from his account
  - Then the new balance is 90.0 EUR

## Stack
- Python 3
  - behave: behaviour-driven development
  - click: beautiful command line interfaces package
  - pytest: unit test framework
  
## Usage

### Install
```
$ virtualenv -p python3 venv
$ source ./venv/bin/activate
$ pip install -r requirements.text
```

### Run
`$ python bank.py [name]`
- -b, --balance
  - Initial account balance

### Tests
- Unit: `$ pytest tests`
- Functional: `$ behave`
