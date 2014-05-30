REDIS_PORT = 6379

BROKER_URL = 'redis://localhost:%s/1' % REDIS_PORT
CELERY_RESULT_BACKEND = 'redis://localhost:%s/0' % REDIS_PORT

BROKER_TRANSPORT_OPTIONS = {
	'fanout_prefix': True,
	'fanout_patterns': True
}

# Here's the magic, polling for results
POLL_URLS = [
	'http://127.0.0.1:1515',
]
