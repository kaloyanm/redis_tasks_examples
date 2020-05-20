import tasks
from redis_tasks.queue import Queue


queue = Queue()
queue.enqueue_call(tasks.count_words_at_url, ['http://www.python.org'])