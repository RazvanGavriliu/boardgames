"""
--- [1] ---
cd "C:\Python36-32\Lib\site-packages\django\bin>"

--- [2] ---
C:\Python36-32\Lib\site-packages\django\bin>python.exe django-admin.py startproject boardgames

--- [3] ---
-> deschid server, pentru a testa

python manage.py runserver

-> apare mesaj migrari

--- [4] ---
-> creez aplicatia cu numele main (apare folder cu numele main)

python manage.py startapp main

--- [5] ---
python manage.py migrate

--- [6] ---
Django admin, ne asiguram ca in boardgames\settings.py "admin" module este enable (nu este comentat)
Apoi poate fi accessat in web utilizand http://localhost:8000/admin/ ; dupa ce am pornit server-ul

--- [7] ---
define New Project in Pycharm; from files already inside folder

--- [8] ---
-> creez cont admin:

C:\Python36-32\Lib\site-packages\django\bin\boardgames>python manage.py createsuperuser --username=razvan --email=razvan1.gavriliu@gmail.com

--- [9] ---
-> ma loghez ca admin:

python manage.py runserver
http://127.0.0.1:8000/admin/login/?next=/admin/

username:
password:

--- [10] ---
-> adaug in "main/views.py" functia >>home<<

--- [11] ---
Acum in "boardgames/url.py" modificam urmatoarele:
	from django.contrib import admin
	from django.urls import path, include
	path('main/', include('main.urls')),

--- [12] ---
-> In main creez: urls.py

-> adaug in fisierul creat [deleg url-urile]:
	from django.contrib import admin
	from django.urls import path, include
	from django.conf.urls import url
	from . import views

	urlpatterns = [
  	  path('admin/', admin.site.urls),
 	   path('', views.home, name="home"),
	]

"""









