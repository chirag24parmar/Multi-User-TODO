# Django
Learning backend using Django. Creating TODO APP using Django .

# Initial setup
1. python -m venv env       // for creating the virtual environment
2. env/Script/activate     // activate virtual enironment
3. create a new folder and cd newforder  
4. pip install djangorestframework     // run command inside the newfolder
5. django-admin startproject main .   // command for initiallization of new project
6. python manage.py migrate         // initial migrate command for migrating default models like admin and etc...
7. python manage.py runserver       // for running the server
# Creating Super user
8. python manage.py createsuperuser // creating the super user({admin,root}) for login in admin pannel
9. python manage.py runserver goto {http://127.0.0.1:8000/admin/} //run the server again and try to login as {admin,root}
# Creating New App 
10. python manage.py startapp home  // creating app (home)
11. go inside project (main/setting.py) inside settings.py update in  { INSTALLED_APPS = ['home'] }
