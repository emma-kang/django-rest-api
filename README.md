# Simple Survey API 
https://stark-citadel-85128.herokuapp.com/api/ <br>
Used Django REST framework 

## Specification 
Python 3.8.2 <br>
Django 3.0.6 <br>
django rest framework 3.11.0 <br>
psycopg2 2.8.5 <br>
django_heroku 0.3.1 <br> 

## Note 
`requirements.txt`, `runtime.txt`, `Procfile` are needed to deploy on Heroku

After push heroku app <br>
Follow command should be ran 
```
heroku run manage.py makemigrations
heroku run manage.py migrate
```

