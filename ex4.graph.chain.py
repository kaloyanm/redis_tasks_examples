import tasks
from redis_tasks.contrib.graph import chain


nodes = [
    dict(func=tasks.count_words_at_url, args=['http://www.python.org']),
    dict(func=tasks.count_words_at_url, args=['https://www.djangoproject.com']),
    dict(func=tasks.total_count), # the last one to be executed
]

graph = chain(nodes)
graph.enqueue()