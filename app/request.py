import urllib.request,json

base_url = None

def configure_request(app):
    global base_url 
    base_url = app.config['API_BASE_URL']