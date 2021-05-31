from getgauge.python import step, before_scenario, Messages
import requests
import os
import json
from step_impl.utils.variables import Variables
from step_impl.utils.response_parse import Parser

# --------------------------
# Gauge step implementations
# --------------------------

@step("set base url <apirul>")
def given_the_request_with_end_point(apiurl):
    base_url = ''
    if apiurl == "test":
       base_url = os.getenv("API_BASE_URL")
    elif apiurl == "test2":
        base_url = os.getenv("API_BASE_URL2")
    Variables.set_base_url(base_url)    


@step("Given the Request with end point <path>")
def given_the_request_with_end_point(path):
    base_url = Variables.get_base_url()
    application_url = f'{base_url}{path}'  
    Variables.set_app_url(application_url)

@step("if a user makes a <method> request")
def if_user_makes_request(method):
    if method == "get":
        print("get")
        response = requests.get(Variables.get_app_url())
        Variables.set_app_response(response)
    elif method == "post":
        print(method)    

@step("Then status is <status>")
def then_status(status):
    response = Variables.get_app_response()
    assert(int(status) == 200)

@step("Then Response contains")
def then_response_contains():
    response = Variables.get_app_response()
    Parser.parse_json(response)


@step("Then <jsonpath> in response contains <value>")
def then_response_contains(jsonpath, value):
    jsonpath_value = Parser.jsonpath_conatins(jsonpath)
    assert(jsonpath_value, value)

@step("set base url for Lamba function <apiurl>")
def then_response_contains(apiurl):
    base_url = ''
    if apiurl == "lambda1":
       base_url = os.getenv("Amazon_Lamda_Function_1_baseUrl")
    elif apiurl == "lambda2":
        base_url = os.getenv("Amazon_Lamda_Function_2_baseUrl")
    Variables.set_base_url(base_url)   





    


