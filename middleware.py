import time


class SleepMiddleware:
    def run_task(self, task, run, args, kwargs):
        time.sleep(1)
        return run(*args, *kwargs)