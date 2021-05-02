# DynaDraw-Gallery
Serverless AWS Backend for DynaDraw

A Serverless Framework Project for a REST HTTP API for CRUD operations on DynamoDB.

serverless deploy --stage dev --region us-east-1
serverless deploy

serverless deploy function --function postMessage --region us-east-1 --stage dev
serverless deploy function --function postMessage

Inspired by - 
https://github.com/fernando-mc/serverless-node-rest-api &
https://github.com/serverless/examples/tree/master/aws-node-rest-api-with-dynamodb