import tasks
from redis_tasks.contrib.graph import TaskGraph


graph = TaskGraph() # Initialize the graph

after_node = graph.add_task(
    dict(func=tasks.total_count))
before_node = graph.add_task(
    dict(func=tasks.count_words_at_url, args=['http://www.python.org']))

graph.add_dependency(before_node, after_node)
graph.enqueue()  # push them into the queue