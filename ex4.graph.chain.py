import tasks
from redis_tasks.contrib.graph import chain


members = [
    dict(func=tasks.count_words_at_url, args=['http://www.python.org']),
    dict(func=tasks.count_words_at_url, args=['https://www.djangoproject.com']),
    dict(func=tasks.total_of_words), # the last one to be executed
]

graph = chain(members)
graph.enqueue()