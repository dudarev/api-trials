Following steps from

https://cloud.google.com/python/django/appengine

## Run locally

To run the example modify all files that have `.example`.

```
pyenv virtualenv drf-gae
pyenv activate drf-gae
pip install -r requirements-vendor.txt -t lib/
pip install -r requirements.txt
```

```
python manage.py makemigrations
python manage.py makemigrations polls
python manage.py migrate
python manage.py createsuperuser
```

```
gcloud auth application-default login
gcloud config setproject <your-project>
```

```
make sql_proxy
```

```
make run
```

## Deploy to Google App Engine

```
python manage.py collectstatic
gcloud app deploy
```
