# This spec contains acceptance tests for verifying api's


## Verify if response contains status 200

* set base url "test"
* Given the Request with end point "/status/200"
* if a user makes a "get" request
* Then status is "200"

## Verify if response contains values

* Given the Request with end point "/status/200"
* if a user makes a "post" request

## Verify if response contains json

* set base url "test2"
* Given the Request with end point "/search?q=title:DNA"
* if a user makes a "get" request
* Then Response contains
