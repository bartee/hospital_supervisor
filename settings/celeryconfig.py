from params import *
from datetime import timedelta

# BROKER_URL is set in the params
# BROKER_URL = 'amqp://'

# CELERY_RESULT_BACKEND is also set in the params
# CELERY_RESULT_BACKEND = 'amqp://'

CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT=['json']
CELERY_TIMEZONE = 'Europe/Amsterdam'
CELERY_ENABLE_UTC = True

CELERY_ANNOTATIONS = {
    'tasks.add': {
    	'rate_limit' : '10/m'
    }
}

beat_schedule = {}

for url in POLL_URLS:
	beat_schedule.update({'check-for-{0}'.format(url): 
		{
	        'task': 'tasks.poll_for_json',
	        'schedule': timedelta(minutes=1),
	        'args': ([url]),
    	}
	})

CELERYBEAT_SCHEDULE = beat_schedule