
class Variables(object):

    app_url = None
    response = None
    base_url = None
    json_response = None

   
    def get_app_url():
        return Variables.app_url
 
    def set_app_url(value):
        Variables.app_url = value    

    def get_base_url():
        return Variables.base_url
 
    def set_base_url(value):
        Variables.base_url = value            

    def get_app_response():
        return Variables.response
 
    def set_app_response(value):
        Variables.response = value            

    def get_app_response_json():
        return Variables.json_response
 
    def set_app_response_json(value):
        Variables.json_response = value    