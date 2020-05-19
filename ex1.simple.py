import settings as proj_settings
import tasks

from redis_tasks.queue import Queue
from redis_tasks.conf import settings
settings.configure(proj_settings)

queue = Queue()
queue.enqueue_call(tasks.count_words_at_url, ['http://www.python.org'])
