hospital_supervisor
===================

Supervisor-project for use with https://github.com/python-hospital/hospital. 
It assumes you have Hospital-serve running on multiple hosts

Getting started
===============
* Create virtualenv, activate it and ``pip install -r requirements.txt``
* Copy ``settings/params_example.py`` to ``settings/params.py``. Check and update redis-settings, and add your own set of urls to poll
* Run ``python celery_app.py beat -s celerybeat-schedule &``. 

