Snoop Project
============

## Snoop Project один из самых перспективных OSINT-инструментов по поиску никнеймов.
- [X] This is the most powerful software taking into account the CIS location.

<img src="https://raw.githubusercontent.com/snooppr/snoop/master/images/snoop.png" />

Snoop project is developed without taking into account the opinions of the NSA and their friends,  
that is, it is available to the average user.

History
https://raw.githubusercontent.com/snooppr/snoop/master/changelog.txt

| Платформа             | Поддержка |
|-----------------------|:---------:|
| GNU/Linux             |     ✅    |
| Windows 7/10 (32/64)  |     ✅    |
| Android/Termux/Andrax |     ✅    |
| macOS                 |     ❗️    |
| IOS                   |     🚫    |
| WSL                   |     🚫    |

[Snoop Full version database 1.1k_websites ⚡️⚡️⚡️](https://github.com/snooppr/snoop/blob/master/websites.md "Database Snoop")  

## Snoop for OS Windows and GNU/Linux  
**Release**  
snoop.exe and snoop
https://github.com/snooppr/snoop/releases

**Native Installation**  
Примечание: Требуемая версия python 3.7 и выше.

```
# Клонировать репозиторий
$ git clone https://github.com/snooppr/snoop

# Войти в рабочий каталог
$ cd ~/snoop

# Установить python3 и python3-pip, если они не установлены
$ apt-get update && apt-get install python3

# Установить зависимости 'requirements'
$ pip install --upgrade pip
$ python3 -m pip install -r requirements.txt
# Либо установить все зависимости из 'requirements.txt' в ручную через
$ pip3 install module
# Если вместо флагов стран отображаются спецсимволы, доставить пакет шрифта, например монохромный
$ apt-get install ttf-ancient-fonts или цветной apt-get install fonts-noto-color-emoji
```
## Snoop for Android
**Native Installation**  

Установить [Termux](https://play.google.com/store/apps/details?id=com.termux&hl=en "Google Play")  
```
# Войти в домашнюю папку Termux (т.е. просто открыть Termux)
$ termux-setup-storage
$ ls #/data/data/com.termux/files/home дефолтный/домашний каталог

# Установить python3 и зависимости
# Примечание: установка продолжительная по времени
$ apt update && pkg upgrade && pkg install python libcrypt libxml2 libxslt git
$ pip install --upgrade pip

# Клонировать репозиторий
$ git clone https://github.com/snooppr/snoop
# (Если флешкa FAT (ни ext4), в таком случае,
# клонировать репозиторий только в ДОМАШНЮЮ директорию Termux)

# Войти в рабочий каталог Snoop
$ cd ~/snoop
# Установить зависимости 'requirements'
$ python3 -m pip install -r requirements.txt


# Дополнение для устаревших гаджетов (Android 6)
# Примечание на современных гаджетах пакеты уже предустановлены и настроены
# добавьте любое 'рандомное' имя и почту [^1]:
$ git config --global user.email "you@example.com"
$ git config --global user.name "username"
# Установите coreutils
$ pkg install coreutils
```
## Using
```
$ python3 snoop.py --help

usage: snoop.py [-h] [--donate y] [--version] [--verbose] [--base]
                [--web-base] [--site] [--time-out] [--found-print] [--no-func]
                [--userload] [--list all] [--country] [--save-report]
                [--update y]
                USERNAMES [USERNAMES ...]

Snoop: поиск никнейма по всем фронтам! (Version 1.2.1_rus Snoop (source demo))

positional arguments:
  USERNAMES             Никнейм разыскиваемого пользователя, поддерживается
                        несколько имён

optional arguments:
  -h, --help            show this help message and exit
  --donate y, -d y      Пожертвовать на развитие Snoop Project-а (получить
                        Snoop Full Version)
  --version, --about, -V
                        НАЧАЛО! Вывод на печать версий: OS; Snoop;
                        Python и Лицензии
  --verbose, -v         Во время поиска 'username' выводить на печать
                        подробную вербализацию
  --base , -b           Указать для поиска 'username' другую БД (Локально)/В
                        demo version функция отключена
  --web-base, -w        Подключиться для поиска 'username' к обновляемой
                        web_БД (Online)
  --site , -s           Указать имя сайта из БД '--list all'. Поиск 'username'
                        на одном указанном ресурсе
  --time-out , -t 9     Установить выделение макс.времени на ожидание ответа
                        от сервера (секунды). Влияет на продолжительность
                        поиска. Влияет на 'Timeout ошибки:'Вкл. эту
                        опцию необходимо практически всегда при медленном
                        интернет соединении, чтобы избежать длительных
                        зависаний при неполадках в сети (по умолчанию значение
                        выставлено 5с)
  --found-print, -f     Выводить на печать только найденные аккаунты
  --no-func, -n         ✓Монохромный терминал, не использовать цвета в url
                        ✓Отключить звук ✓Запретить открытие web browser-а
                        ✓Отключить вывод на печать флагов стран ✓Отключить
                        индикацию и статус прогресса
  --userload , -u       Указать файл со списком user-ов. Пример_Linux:
                        'python3 snoop.py -u ~/listusers.txt start' Пример для
                        Windows: 'python snoop.py -u c:\snoop\listusers.txt
                        start'
  --list all            Вывести на печать информацию о локальной базе данных
                        Snoop
  --country, -c         Сортировка 'вывода на печать/запись_результатов' по
                        странам, а не по алфавиту
  --save-report, -S     Сохранять найденные странички пользователей в
                        локальные файлы
  --update y            Обновить Snoop
```

**Example**
```
# Для поиска только одного пользователя:
$ python3 snoop.py username1
# Или, например, кириллица поддерживается:
$ python3 snoop.py олеся
# Для поиска имени, содержащего пробел:
$ python3 snoop.py "ivan ivanov"
$ python3 snoop.py ivan_ivanov
$ python3 snoop.py ivan-ivanov

# Запуск на OS Windows:
$ python snoop.py username1

# Для поиска одного и более юзеров:
$ python3 snoop.py username1 username2 username3 username4

# Поиск множества юзеров — сортировка вывода результатов по странам;
# избежание зависаний на сайтах (чаще 'мёртвая зона' зависит от вашего ip-адреса);
# выводить на печать только найденные аккаунты; сохранять странички найденных
# аккаунтов локально; указать файл со списком разыскиваемых аккаунтов:
$ python3 snoop.py -с -t 13 -f -S -u ~/file.txt start

# 'ctrl-c/z' — прервать поиск
```
Найденные учетные записи будут храниться в ~/snoop/results/*/username.{txt.csv.html}.  
Для доступа браузера к результатам поиска на платформе Android требуются рут права.  
csv открывать в *office в кодировке utf-8, разделитель 'запятая'.  

Уничтожить **все** результаты поиска — удалить каталог '~/snoop/results'.  

При запуске Snoop с ключом '-S' все страницы сохраняются локально в кодировке 'utf-8'.  
Некоторые сайты используют другие кодировки, например, 'windows-1251',  
сохранённые кодовые страницы (меньшинство таких) могут отображать 'кракозябры',  
чтобы восстановить читабельность страниц, пересохранить файл, например,  
```
$ iconv -f utf-8 -t windows-1251 'snoop/results/save reports/username/Igromania.html' > NewIgromania.html
```

```
# Обновляйте Snoop для тестирования новых функций в ПО:
$ python3 snoop.py --update y
[^1]: Требуется установка Git.
```

<img src="https://raw.githubusercontent.com/snooppr/snoop/master/images/Run.gif"/>  

<img src="https://raw.githubusercontent.com/snooppr/snoop/master/images/snoopandroid.png" />

<img src="https://raw.githubusercontent.com/snooppr/snoop/master/images/snoop_run.png" />

## Основные ошибки  

|  Сторона  |                         Проблема                      | Решение |
|:---------:| ------------------------------------------------------|:-------:|
| ========= |=======================================================| ======= |
| Клиент    |Блокировка соединения проактивной защитой (*Kaspersky) |    1    |
|           |Недостаточная скорость интернет соединения EDGE / 3G   |    2    |
|           |Слишком низкое значение опции '-t'                     |    2    |
|           |недопустимое username                                  |    3    |
|           |Ошибки: [GipsysTeam; RamblerDating; Mamochki]          |    7    |
| ========= |=======================================================| ======= |
| Провайдер |Internet Censorship                                    |    4    |
| ========= |=======================================================| ======= |
| Сервер    |Cайт изменил свой ответ/API; обновился CF/WAF          |    5    |
|           |Блокировка сервером диапазона ip-адресов клиента       |    4    |
|           |Срабатывание/защита ресурса captch-ей                  |    4    |
|           |Некоторые сайты временно недоступны, технические работы|    6    |
| ========= |=======================================================| ======= |

Решения:
1. Перенастроить свой Firewall (например, Kaspersky блочит Ресурсы для взрослых).

2. Проверить скорость своего интернет соединения:  
$ python3 snoop.py -v username  
Если какой-либо из параметров сети выделен красным цветом, Snoop может повиснуть во время поиска.  
При низкой скорости увеличить значение опции '--time x':  
$ python3 snoop.py -t 15 username  

3. Фактически это не ошибка. Исправить username  
(например, на некоторых сайтах недопустимы символы кириллицы; "пробелы"; или 'вьетнамо-китайская_кодировка'  
в именах пользователей, в целях экономии времени: — запросы фильтруются).

4. **Сменить свой ip-адрес**  
("Серый" ip и цензура - самое частое из-за чего вы получаете ошибки пропуска/ложного срабатывания/и в некоторых случаях '**Увы**'.  
Например, самый действенный способ решить проблему — использовать VPN, Tor не очень хорошо подходит для данной задачи.  
Правило: одного сканирования с одного ip недостаточно для получения макимальной отдачи от Snoop).

5. Открыть в Snoop репозитории на Github-e Issue/Pull request  
(сообщить об этом разработчику).

6. Не обращать внимание, сайты иногда уходят на ремонтные работы и возвращаются в строй.

7. [Проблема](https://wiki.debian.org/ContinuousIntegration/TriagingTips/openssl-1.1.1 "проблема простая и решаемая") с некоторыми дистрибутивами GNU/Linux  
Решение
```
$ sudo nano /etc/ssl/openssl.cnf

# Изменить в самом низу файла строки:
[CipherString = DEFAULT@SECLEVEL=2]
на
[CipherString = DEFAULT@SECLEVEL=1]
```

**Отпечаток публичного ключа:**	[076DB9A00B583FFB606964322F1154A0203EAE9D](https://raw.githubusercontent.com/snooppr/snoop/master/PublicKey.asc "pgp key")

**Лицензия Snoop Project:** https://github.com/snooppr/snoop/blob/master/COPYRIGHT

[Документация](https://drive.google.com/open?id=12DzAQMgTcgeG-zJrfDxpUbFjlXcBq5ih)

**SNOOP PROJECT (OSINT) СУЩЕСТВУЕТ И РАЗВИВАЕТСЯ ТОЛЬКО НА GITHUB. НИ К TELEGRAM, НИ К WEB/ONLINE SNOOP НЕ ИМЕЕТ НИКАКОГО ОТНОШЕНИЯ.**

**В СВЯЗИ СО СЛОЖИВШЕЙСЯ СИТУАЦИЕЙ В МИРЕ (САМОИЗОЛЯЦИЯ ГРАЖДАН ИЗ ЗА ЭПИДЕМИИ) СИЛЬНО ВЫРОСЛА НАГРУЗКА НА СЕТИ. SNOOP В ДАННЫЙ ПЕРИОД МОЖЕТ РАБОТАТЬ МЕДЛЕННО.**
