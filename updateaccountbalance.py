import json
import account_validation as validationlayer

def lambda_handler(event, context):
    if validationlayer.validateAcct(event['AcctNo']) == 'PASS':
        return updateAccountBalance(event['AcctNo'], event['Amount'])
    else:
        return {'status': 'FAIL', 'message': 'Bad Account Number'}

def updateAccountBalance(acct_no, amount):
    # Simulate updating account balance
    updated_balance = 1000 + amount  # Example calculation
    return {'status': 'PASS', 'AcctNo': acct_no, 'UpdatedBalance': updated_balance}
