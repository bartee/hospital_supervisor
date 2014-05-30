from settings.params import *
from celery import Celery
import tasks

app = Celery('tasks', backend=CELERY_RESULT_BACKEND, broker=BROKER_URL)

app.config_from_object('settings.celeryconfig')

if __name__ == '__main__':
    app.start()