super user  zheming wamt123456

## installation
pip install django
pip install django-crispy-forms

## create new project
django-admin startproject mysite 

cd mysite <strong> go to path under mysite this is the place you input commands below<strong> 

python manage.py createsuperuser --username=<your username>
## when you change the models
python manage.py makemigration 

python manage.py migrate
## this is the command to start server
python manage.py runserver

