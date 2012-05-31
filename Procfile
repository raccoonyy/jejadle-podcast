web: bin/gunicorn_django --workers=4 --bind=0.0.0.0:$PORT jejadlepod/settings.py
worker: bin/python jejadlepod/manage.py celeryd -E -B --loglevel=INFO
