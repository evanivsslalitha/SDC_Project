import json
import account_validation as validationlayer

def lambda_handler(event, context):
    if validationlayer.validateAcct(event['AcctNo']) == 'PASS':
        return createAccount(event['AcctNo'])
    else:
        return {'status': 'FAIL', 'message': 'Bad Account Number'}

def createAccount(acct_no):
    # Simulate account creation process
    account_data = {
        'AcctNo': acct_no,
        'Balance': 0,
        'Status': 'Active'
    }
    return {'status': 'PASS', 'message': 'Account created successfully', 'account': account_data}
