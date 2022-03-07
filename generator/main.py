import requests
import time

def curl():
    # url = os.environ['URL']
    url = 'http://web:5000'
    resp = requests.get(url, timeout=1)
    resp2 = requests.post(url, timeout=1)
    # print(resp.status_code)
    # print(resp.text)

if __name__ == '__main__':
    while True:
        curl()
        time.sleep(1)
