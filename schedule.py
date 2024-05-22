import time
from apscheduler.schedulers.blocking import BlockingScheduler

def job():
    print("Hello, World!")

scheduler = BlockingScheduler()
scheduler.add_job(job, "interval", seconds=2)
scheduler.start()