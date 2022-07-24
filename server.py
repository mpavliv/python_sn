import requests
url = '185.65.246.123:'
url = 'http://185.65.246.123:8080/sn'

def send_request(sn):
    print('starting request to ' + url)
    headers = {'Content-Type': 'text/plain; charset=UTF-8'}
    for el in sn:
        x = requests.post(url, data=el.encode('utf-8'), headers=headers, timeout=20)


    print('data sent')


