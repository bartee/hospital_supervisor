from celery_app import app

@app.task
def poll_for_json(url):
	"""
	Poll for a given url, expect a JSON response back. That will be stored in the backend.

	- Catches a URLError in case it cannot be found
	- Catches a ValueError in case of invalid feedback
	- Catches all other exceptions

	:param url: the url to poll
	"""
	import urllib2
	import json

	req = urllib2.Request(url)
	opener = urllib2.build_opener()
	try:
		f = opener.open(req)
		return json.load(f)
	except urllib2.URLError,e:
		res = {
			'status': 'fail',
			'details': {'Supervisor': 'Unable to connect: %s' % e},
			'summary': 'Unable to connect to %s ' % url
		}
		return res
	except ValueError, e:
		res = {
			'status': 'fail',
			'details': {'Supervisor': 'Call returned no JSON: %s' % e},
			'summary': 'Invalid response from %s ' % url
		}
		return res
	except Exception, e:
		res = {
			'status': 'fail',
			'details': {'Supervisor': 'Uncaught exception thrown: %s' % e},
			'summary': 'No clue as of yet what went wrong at %s ' % url
		}
		return res