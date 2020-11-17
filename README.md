#### Развертывание сайта локально:
```
1) user@user-pc:~/Downloads$ python3 -m venv django_test
2) user@user-pc:~/Downloads/django_test/bin$ source activate
3) (django_test) user@user-pc:~/Downloads/django_test$ pip3 install django
4) (django_test) user@user-pc:~/Downloads/django_test$ django-admin startproject my_site .
5) (django_test) user@user-pc:~/Downloads/django_test$ python manage.py startapp p_library
6) создать в директории django_test/my_site файл .env со значением SECRET_KEY из settings.py, например:
   SECRET_KEY=0g#3f26r@j!wjb78-(x%f5kw#e%vid5b^u^mr_x^fajwbn^%@-
7) скачать zip-архив данного приложения, разархивировать в django_test с перезаписью целевых файлов
8) (django_test) user@user-pc:~/Downloads/django_test$ pip3 install -r requirements.txt
9) (django_test) user@user-pc:~/Downloads/django_test$ python manage.py runserver
```

#### Данные суперпользователя БД
```
user: admin
password: 1
```
