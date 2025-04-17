import json
import account_validation as validationlayer

def lambda_handler(event, context):
    if validationlayer.validateAcct(event['AcctNo']) == 'PASS':
        return getAccountBalance(event['AcctNo'])
    else:
        return {'status': 'FAIL', 'message': 'Bad Account Number'}

def getAccountBalance(acct_no):
    # Simulate fetching account balance
    account_balance = 1000  # Example balance value
    return {'status': 'PASS', 'AcctNo': acct_no, 'Balance': account_balance}
