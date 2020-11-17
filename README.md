#### Развертывание сайта локально:
```
1) user@user-pc:~/Downloads$ python3 -m venv django_test

2) скачать zip-архив данного приложения, разархивировать в django_test

3) создать в директории django_test/my_site файл .env с содержимым:
SECRET_KEY = 'kqw=m9&v29xxy+irop@ozxk&f^u(j+&r)qb#u%1if2+3-iu0)p'

4) user@user-pc:~/Downloads/django_test/bin$ source activate

5) (django_test) user@user-pc:~/Downloads/django_test$ pip3 install -r requirements.txt

6) (django_test) user@user-pc:~/Downloads/django_test$ python manage.py runserver
```

#### Данные суперпользователя БД
```
user: admin
password: 1
```
