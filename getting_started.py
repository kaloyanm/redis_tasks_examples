import requests

def count_lines_in_url(url):
    resp = requests.get(url)
    print(len(resp.text))
