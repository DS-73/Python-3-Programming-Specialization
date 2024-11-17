import requests_with_caching

def get_joke_data(term):
    import json
    URL = 'https://icanhazdadjoke.com/search'
    params = {
        'term':term,
        'limit':2
    }
    
    headers = {
        "Accept": "application/json"
    }
    
    response = requests_with_caching.get(baseurl=URL, params=params, headers=headers)
    print(response.text)
print(get_joke_data('magic'))