# Quick config to manage a superset server & worker

### Initiate
- `pip install pipenv`
- `pipenv --two && pipenv shell` (as the time of writing, superset is more stable on py2)
- `pipenv install`

### Run
- `supervisord`
- See `supervisord.conf` and `superset_config.py` for more

### Manage
- `supervisorctl`

### Caveat
- As the time of writing, `superset runserver` calls gunicorn, which will not be stopped when supervisor stops superset
  - Manual: `ps aux | grep gunicorn`, find the pid, and `kill -9 <pid>`
