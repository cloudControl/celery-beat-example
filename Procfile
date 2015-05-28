web: (cd public ; python -m http.server $PORT)
worker: celery -A tasks worker -B -E --loglevel=info
