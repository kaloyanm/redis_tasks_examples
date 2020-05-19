import settings as proj_settings
import tasks

from redis_tasks.contrib.graph import TaskGraph
from redis_tasks.queue import Queue
from redis_tasks.conf import settings
settings.configure(proj_settings)

# Create the graph
graph = TaskGraph()
urls_to_inspect = [
    'http://www.python.org',
    'https://www.djangoproject.com',
    'https://flask.palletsprojects.com/en/1.1.x/',
]

# Manually con
final_node = graph.add_task(dict(func=tasks.total_of_words))
for url in urls_to_inspect:
    node = graph.add_task(dict(func=tasks.count_words_at_url, args=[url]))
    graph.add_dependency(node, final_node)
graph.enqueue()  # push them into the queue
