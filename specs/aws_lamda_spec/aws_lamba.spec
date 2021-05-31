# This spec contains acceptance tests for aws lamda functions created

Pre-Requiste - Create an API using Amazon API Gateway for the lamba functions


## Verify if response contains status 200

* set base url for Lamba function "lamda1"
* Given the Request with end point "/status/200"
* if a user makes a "get" request
* Then status is "200"
