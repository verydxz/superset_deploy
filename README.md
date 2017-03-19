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
- As the time of writing, `superset runserver` calls gunicorn, which will not be stopped when you ask supervisor to stop superset process
  - Manual: `ps aux | grep gunicorn`, find the pid, and `kill -9 <pid>`
