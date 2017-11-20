"""
reference: https://github.com/airbnb/superset/blob/master/superset/config.py
"""

import os
from werkzeug.contrib.cache import FileSystemCache

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATA_DIR = os.path.join(os.path.expanduser('~'), '.superset')
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)
# uncomment below if don't want to use the default superset db in 'DATA_DIR'
# SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'superset.db')

APP_NAME = "Viz"
SECRET_KEY = 'whoareyoubaby'
MAPBOX_API_KEY = 'pk.eyJ1IjoidmVyeWR4eiIsImEiOiJjamE4OXQ2eXgwNThiMzNxODlkdzV2YjRlIn0.YqbVdVEn5S4eTFGcuJNJyA'

SUPERSET_WORKERS = 2

SUPERSET_CELERY_WORKERS = 8
class CeleryConfig(object):
    BROKER_URL = 'sqla+sqlite:///celery.d/celerydb.sqlite'
    CELERY_IMPORTS = ('superset.sql_lab', )
    CELERY_RESULT_BACKEND = 'db+sqlite:///celery.d/celery_results.sqlite'
    CELERY_ANNOTATIONS = {'tasks.add': {'rate_limit': '10/s'}}
CELERY_CONFIG = CeleryConfig

RESULTS_BACKEND = FileSystemCache('/tmp/sqllab_cache', default_timeout=60)
