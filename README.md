#### Развертывание сайта локально:
```
1) user@user-pc:~/Downloads$ python3 -m venv django_test

2) user@user-pc:~/Downloads$ cd django_test/bin

3) user@user-pc:~/Downloads/django_test/bin$ source activate

4) (django_test) user@user-pc:~/Downloads/django_test/bin$ cd ..

5) (django_test) user@user-pc:~/Downloads/django_test$ pip3 install django

6) (django_test) user@user-pc:~/Downloads/django_test$ django-admin startproject my_site .

7) (django_test) user@user-pc:~/Downloads/django_test$ python manage.py startapp p_library

8) создать в директории django_test/my_site файл .env со значением SECRET_KEY из settings.py, например:
SECRET_KEY = 'kqw=m9&v29xxy+irop@ozxk&f^u(j+&r)qb#u%1if2+3-iu0)p'

9) скачать zip-архив данного приложения, разархивировать в django_test с перезаписью целевых файлов

10) (django_test) user@user-pc:~/Downloads/django_test$ pip3 install -r requirements.txt

11) (django_test) user@user-pc:~/Downloads/django_test$ python manage.py runserver
```

#### Данные суперпользователя БД
```
user: admin
password: 1
```
