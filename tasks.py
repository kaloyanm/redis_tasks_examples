import requests
from redis_tasks import redis_task

@redis_task()
def count_lines_in_url(url):
    resp = requests.get(url)
    print(len(resp.text))
