import tasks

from redis_tasks.contrib.graph import chain
from redis_tasks.conf import settings

settings.configure_from_dict(
    {'MIDDLEWARE': ['redis_tasks.contrib.graph.GraphMiddleware']})


urls_to_inspect = [
    'http://www.python.org',
    'https://www.djangoproject.com',
    'https://flask.palletsprojects.com/en/1.1.x/',
]
members = []
for url in urls_to_inspect:
    members.append(dict(func=tasks.count_words_at_url, args=[url]))
members.append(dict(func=tasks.total_of_words))

graph = chain(members)
graph.enqueue()