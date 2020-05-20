import time
import smtplib
from email.message import EmailMessage

class SleepMiddleware:
    def run_task(self, task, run, args, kwargs):
        time.sleep(1)
        run(*args, *kwargs)


class ReportMiddleware:
    def process_outcome(self, task, *exc_info):
        msg = EmailMessage()
        msg['Subject'] = 'Daily Report'
        msg['From'] = 'development@test.com'
        msg['To'] = 'client@test.com'

        s = smtplib.SMTP('localhost')
        s.send_message(msg)
        s.quit()