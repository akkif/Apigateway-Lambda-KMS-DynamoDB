# Apigateway-Lambda-KMS-DynamoDB

**What does this code do**

 - this is a python 3.* code
 - lambda function takes email and password from the event
 - encrypts the password using kms key
 - puts email and encrypted password
 - then retrieves the email and the encrypted password
 - decrypts the password 
 - returns the decrypted password

**how to use this code**

 - paste the code on the lambda function 
 - replace kms key and table name.
 - create a apigateway with post method and send email and password in the request body
 -make sure to integrate the apigatway with relevant lambda function
 

 - add a dynamodb table with email primary key and declare it as string.
 - you are good to go

 

