from datetime import timedelta
from params import *

beat_schedule = {}

for url in POLL_URLS:
	schedule.update({'check-for-{0}'.format(url): 
		{
	        'task': 'tasks.poll_for_json',
	        'schedule': timedelta(minutes=1),
	        'args': (url),
    	}
	})

CELERYBEAT_SCHEDULE = beat_schedule