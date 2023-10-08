import requests

def send_request(url, method='GET', headers=None, data=None):
    try:
        response = requests.request(method, url, headers=headers, data=data)
        return response.status_code, response.text
    except requests.exceptions.RequestException as e:
        print(f'Error: {e}')