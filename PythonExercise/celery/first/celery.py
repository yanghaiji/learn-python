from __future__ import absolute_import

from celery import Celery

app = Celery('first', include=['first.tasks'])

app.config_from_object('first.celeryconfig')


if __name__ == '__main__':

    app.start()