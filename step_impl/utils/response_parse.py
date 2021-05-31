import json
from jsonpath_ng import jsonpath, parse
from step_impl.utils.variables import Variables

class Parser(object):

    def parse_json(json_data):
        json_parse = ''
        if json_data.status_code == 200:
            json_parse = json.loads(json_data.text)
            Variables.set_app_response_json(json_parse)       
    
    def jsonpath_contains(json_path):
        jsonpath_expression = parse('$.id')
        match = jsonpath_expression.find(Variables.get_app_response_json())
        print(match)






        