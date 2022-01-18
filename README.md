# onliner_refresher
Скрипт для обновления объявлений на onliner.by

Работает на Windows / Linux(Ubuntu) / Mac OS

Для Windows, просто измените путь в переменной:

>__service = Service('/usr/bin/chromedriver') на service = Service('C:\Files\chromedriver.exe')__

Библиотеки необходимые для работы скрипта:

1. __Selenium__
2. __PyVirtualDisplay__
3. __Urllib3__

Необходимо указать логин в переменную __Login = 'example@mail.com'__ и пароль __Password = 'qwerty123'__

Для того чтобы всё работало автоматически, создайте задачу в cron через команду crontab -e.

Задайте условие */30 * * * * /usr/bin/python3.8 -u /path/where/locate/script/onliner.py >> /path/where/locate/log/crontab_chromedriver_error.log 2>&1 и сохраните.
