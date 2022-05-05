# yatube

Прототип социальной сети yatube. Сеть предназначена для публикации и комментирования сообщений, поддерживает механизм подписки.

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/Offlinexaa/yatube_project.git
```

```
cd yatube_project
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

```
source venv/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip setuptools pillow
```

```
pip install -r requirements.txt
```

Подготовить и выполнить миграции:

```
python3 manage.py makemigrations
```

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

### Требования

Python 3.7 или выше

Django 2.2.24

pytz 2021.3

sqlparse 0.4.2
