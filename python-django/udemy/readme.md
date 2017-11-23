python-3-na-web-com-django-basico-intermediario

1. prepare enviroment
   1. install python3
   1. install python-pip
   1. install python-setuptools
   1. install python-virtualenv
   1. enter folder ./project/venv/bin. Enter command ". activate"
   1. install python-django / pip install django==1.6 
   1. test installation of django: type python, import django.
      1. if error occurred: try setting up enviroment variable PYTHONPATH
      1. type "echo $PYTHONPATH" (probably will return blank)
      1. find installation directory: /usr/lib/python3/dist-packages
      1. type "export PYTHONPATH=path-of-installation-directory"
      1. test with the same command in step 2. Test with same step of import.
      1. if using ṕython 3 or above, download the latest version of django. Ex: 1.8, 2.0, 2.1. They have support for python 3.
      1. start the server by running the command: "python manage.py name-of-your-project".
         1. if the error: "django.db.utils.OperationalError: unable to open database file" appears, just start the command with "sudo"


