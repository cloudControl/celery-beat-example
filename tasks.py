from datetime import datetime, timedelta
from os import environ

from celery import Celery, task

celery = Celery('tasks', broker='sqla+mysql+pymysql://{}:{}@{}:3306/{}'.format(
    environ.get('MYSQLS_USERNAME'), environ.get('MYSQLS_PASSWORD'),
    environ.get('MYSQLS_HOSTNAME'), environ.get('MYSQLS_DATABASE')))

celery.conf.update(
    CELERYBEAT_SCHEDULE = {
        'now': {
            'task': 'tasks.now',
            'schedule': timedelta(seconds=10)
        },
    }
)

@task
def now():
    print(str(datetime.now()))
