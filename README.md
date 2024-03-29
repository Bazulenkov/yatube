# Социальная сеть для публикации личных дневников

## Возможности
- Можно зарегистрироваться как автор и создать свою страницу;
- Авторы могут создавать статьи;
- Статьи можно помещать в тематические группы;
- К каждой статье можно прикрепить фото-обложку;
- Если зайти на страницу автора:
  - то можно посмотреть все записи автора;
  - подписаться на автора; 
  - комментировать статьи автора;
- На главной странице во вкладке "Избранные авторы" отображаются статьи только тех авторов, на которых подписан пользователь

## Установка
Эти инструкции помогут вам создать копию проекта и запустить ее на локальном компьютере для целей разработки и тестирования.

### Запуск проекта (на примере Linux)

Перед тем, как начать: если вы не пользуетесь `Python 3`, вам нужно будет установить инструмент `virtualenv` при помощи `pip install virtualenv`. 
Если вы используете `Python 3`, у вас уже должен быть модуль [venv](https://docs.python.org/3/library/venv.html), установленный в стандартной библиотеке.

- Создайте на своем компютере папку проекта blog `mkdir blog` и перейдите в нее `cd blog`
- Склонируйте этот репозиторий в текущую папку `git clone https://github.com/Bazulenkov/yatube.git`
- Создайте виртуальное окружение `python3 -m venv venv`
- Активируйте виртуальное окружение `source venv/bin/activate`
- Установите зависимости `pip install -r requirements.txt`
- Примените миграции `python manage.py migrate`
- Создайте суперпользователя Django `python manage.py createsuperuser --username admin --email 'admin@example.com'`
- Запустите сервер разработки Django `python manage.py runserver`

## В разработке использованы

- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [Pillow](https://pypi.org/project/Pillow/)
- [Sorl-thumbnail](https://pypi.org/project/sorl-thumbnail/)
- [Django-debug-toolbar](https://pypi.org/project/django-debug-toolbar/)


## Мониторинг доступности и сбор ошибок
- [UptimeRobot](https://uptimerobot.com)
- [Sentry](https://sentry.io/)

