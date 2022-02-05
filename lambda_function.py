import boto3
from boto3.session import Session
from boto3.dynamodb.conditions import Key, Attr
import base64


kms = boto3.client('kms')  
dynamodb = boto3.resource('dynamodb')
table= dynamodb.Table('T a b l e  n a m e')
def lambda_handler(event, context):
    KeyId= 'K M S   K E Y'
    
    print("###########event##########")
    print(event)
    email=event['email']
    password=event['password']
    print(email)
    print(password)
    
    ####KMS encryption#####################
    enc_result= kms.encrypt(
    KeyId=KeyId,
    Plaintext=password)
    
    blob=enc_result['CiphertextBlob']
    #print(f'blob {blob}')
    final_password = (base64.b64encode(blob))
    
    ###putting data on dynamodb
    response = table.put_item(Item={
        'email':email,
        'password':final_password
    })
    
    ##get password from database
    beforekey = table.get_item(Key={'email':email})
    print(beforekey)
    
    ##decrypt
    print(beforekey['Item']['password'].value)
    print(kms.decrypt(CiphertextBlob = base64.b64decode(beforekey['Item']['password'].value))['Plaintext'])
    print("---")
    afterkey = kms.decrypt(CiphertextBlob = base64.b64decode(beforekey['Item']['password'].value))['Plaintext']
    return afterkey
