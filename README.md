# Quick config to manage a superset server & worker

### Initiate
- `pip install pipenv`
- `pipenv --two && pipenv shell` (as the time of writing, superset is more stable on py2)
- `pipenv install`

### Run
- `supervisord`
- See `supervisord.conf` and `superset_config.py` for more
- BTW, you may want to [initialize superset](http://airbnb.io/superset/installation.html#superset-installation-and-initialization) first

### Manage
- `supervisorctl`
- For example, `supervisorctl stop all`

### Caveat
- `Pipfile.lock` is a workable version, but if you want to use newer versions, just delete it before `pipenv install`
- `superset runserver` calls gunicorn, sometimes the sub group processes will not be stopped when you ask supervisor to stop superset process
  - Manual: `ps aux | grep gunicorn`, find the pid, and `kill -9 <pid>`
