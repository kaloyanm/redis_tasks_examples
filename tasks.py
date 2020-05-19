import requests
from redis_tasks import redis_task

@redis_task()
def count_words_at_url(url):
    resp = requests.get(url)
    print(len(resp.text.split()))


@redis_task()
def total_of_words():
    pass
