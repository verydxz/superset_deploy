"""
reference: https://github.com/airbnb/superset/blob/master/superset/config.py
"""

import os
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

# celery workers for sqllab
SUPERSET_CELERY_WORKERS = 8

class CeleryConfig(object):
    BROKER_URL = 'redis://localhost:6379/1'
    CELERY_IMPORTS = ('superset.sql_lab', )
    CELERY_RESULT_BACKEND = 'redis://localhost:6379/1'
    CELERY_ANNOTATIONS = {'tasks.add': {'rate_limit': '10/s'}}
CELERY_CONFIG = CeleryConfig

# result backend for sqllab
import werkzeug.contrib.cache
RESULTS_BACKEND = werkzeug.contrib.cache.RedisCache(
    host='localhost', port=6379, db=2, key_prefix='superset_results', default_timeout=3600)

# cache for reports
CACHE_CONFIG = {
    'CACHE_TYPE': 'redis',
    'CACHE_KEY_PREFIX': 'superset_cache',
    'CACHE_REDIS_URL': 'redis://localhost:6379/3'
}
CACHE_DEFAULT_TIMEOUT = 300
