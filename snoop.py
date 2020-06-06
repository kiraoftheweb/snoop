#! /usr/bin/env python3
# Copyright (c) 2020 Snoop Project <snoopproject@protonmail.com> 

import base64
import certifi
import csv
import json
import locale
import networktest
import os
import platform
import random
import re
import requests
import subprocess
import sys
import time
import webbrowser

from argparse import ArgumentTypeError
from argparse import ArgumentParser, RawDescriptionHelpFormatter
from collections import Counter
from colorama import Fore, Style, init
from concurrent.futures import ThreadPoolExecutor
from playsound import playsound
from requests_futures.sessions import FuturesSession
try:
    from rich.progress import (BarColumn, Progress,TimeRemainingColumn)
except ModuleNotFoundError:
    print(f"Установить модуль 'rich', в GNU команда:\n" + \
    Style.BRIGHT + Fore.RED + "cd ~/snoop && python3 -m pip install -r requirements.txt" + \
    Style.RESET_ALL)
    sys.exit(0)

if sys.platform == 'win32':
    locale.setlocale(locale.LC_ALL, '')
init(autoreset=True)

print ("""\033[36m
  ___|                          
\___ \  __ \   _ \   _ \  __ \  
      | |   | (   | (   | |   | 
_____/ _|  _|\___/ \___/  .__/  
                         _|    \033[0m \033[37mv1.2.1\033[34;1m_rus_\033[31;1mSource Demo\033[0m
""")

if sys.platform == 'win32':
	print (Fore.CYAN + "#Example:" + Style.RESET_ALL)
	print (Fore.CYAN + " cd с:\snoop" + Style.RESET_ALL)	
	print (Fore.CYAN + " python snoop.py --help" + Style.RESET_ALL, "#reference")
	print (Fore.CYAN + " python snoop.py username" + Style.RESET_ALL, "#Search user-a")
	print (Fore.CYAN + "============================================\n" + Style.RESET_ALL)
else:
	print (Fore.CYAN + "#Example:" + Style.RESET_ALL)
	print (Fore.CYAN + " cd ~/snoop" + Style.RESET_ALL)
	print (Fore.CYAN + " python3 snoop.py --help" + Style.RESET_ALL, "#reference")
	print (Fore.CYAN + " python3 snoop.py username" + Style.RESET_ALL, "#Example user-a")
	print (Fore.CYAN + "=============================================\n" + Style.RESET_ALL)

module_name = (Fore.CYAN + "Snoop: nickname search on all fronts!" + Style.RESET_ALL)
version = "1.2.1_rus Snoop (source demo)"

dirresults = os.getcwd()
timestart = time.time()
time_data = time.localtime()
censor = 0

def fff():
    try:
        with open('BDdemo', "r", encoding="utf8") as z:
            dd = z.read() 
            b1 = dd.encode("UTF-8") 
            d1 = base64.b64decode(b1) 
            rt1 = d1[::-1] 
            d2 = base64.b64decode(rt1)
            s12 = d2.decode("UTF-8") 
            bbb1 = json.loads(s12) 
            return bbb1
    except:
        print(Style.BRIGHT + Fore.RED + "Oops, something went wrong..." + Style.RESET_ALL)
        sys.exit(0)

def kkk():
    try:
        with open('BDflag', "r", encoding="utf8") as z1:
            d11 = z1.read()
            b11 = d11.encode("UTF-8") 
            t11 = base64.b64decode(b11) 
            rt11 = t11[::-1] 
            d22 = base64.b64decode(rt11)
            s112 = d22.decode("UTF-8") 
            ccc1 = json.loads(s112) 
            return ccc1
    except:
        print(Style.BRIGHT + Fore.RED + "Oops, something went wrong..." + Style.RESET_ALL)
        sys.exit(0)

# Флаг БС
def baza():
    BS = fff()
    flagBS = len(BS)
    return BS
flagBS = len(baza())

# Создание директорий результатов.
try:
    os.makedirs(str(dirresults + "/results"))
except:
    pass
try:
    os.mkdir(str(dirresults + "/results/html"))
except:
    pass
try: 
    os.mkdir(str(dirresults + "/results/txt"))
except:
    pass
try:
    os.mkdir(str(dirresults + "/results/csv"))
except:
    pass
try:
    os.makedirs(str(dirresults + "/results/save reports"))
except:
    pass

################################################################################
class ElapsedFuturesSession(FuturesSession):
    """test_metrica"""
    def request(self, method, url, *args, **kwargs):
        """test"""
        return super(ElapsedFuturesSession, self).request(method, url, *args, **kwargs)

def print_info(title, info, color=True):
    if color:
        print(Fore.GREEN + "[" +
            Fore.YELLOW + "*" +
            Fore.GREEN + f"] {title}" +
            Fore.RED + "\033[5m <\033[0m" +
            Fore.WHITE + f" {info}" +
            Fore.RED + "\033[5m >\033[0m")
    else:
        print(f"\n[*] {title} {info}:")


def print_error(err, errstr, var, verbose=False, color=True):
    if color:
        print(Fore.CYAN + "[" +
            Style.BRIGHT + Fore.RED + "-" + Style.RESET_ALL +
            Fore.CYAN + "]" +
            Style.BRIGHT + Fore.RED + f" {errstr}" +
            Style.BRIGHT + Fore.YELLOW + f" {err if verbose else var}")
        try:
            playsound('err.wav')
        except:
            pass
    else:
        print(f"[-] {errstr} {err if verbose else var}")


# Printing on different platforms.
if sys.platform == 'win32':
    def print_found_country(social_network, url, countryB, response_time=False, verbose=False, color=True):
        if color:
            print(Style.BRIGHT + Fore.CYAN + f" {countryB}" + 
                Fore.GREEN + f" {social_network}:", url)
        else:
            print(f"[+] {social_network}: {url}")
else:            
    def print_found_country(social_network, url, countryA, response_time=False, verbose=False, color=True):
        if color:
            print(countryA, (Style.BRIGHT +
                Fore.GREEN + f" {social_network}:"), url)
        else:
            print(f"[+] {social_network}: {url}")


def print_not_found(social_network, response_time, verbose=False, color=True):
    if color:
        print((Fore.CYAN + "[" +
            Style.BRIGHT + Fore.RED + "-" + Style.RESET_ALL +
            Fore.CYAN + "]" +
            Style.BRIGHT + Fore.GREEN + f" {social_network}:" +
            Style.BRIGHT + Fore.YELLOW + " Увы!"))
    else:
        print(f"[-] {social_network}: Увы!")


def print_invalid(mes, social_network, message, color=True):
    """Ошибка вывода результата"""
    if color:
        print((Fore.RED + "............[" +
            Style.BRIGHT + Fore.RED + "-" + Style.RESET_ALL +
            Fore.RED + "]" +
            Style.BRIGHT + Fore.GREEN + f" {social_network}:" +
            Style.RESET_ALL + Fore.YELLOW + f" {message}"))
    else:
        print(f"[-] {social_network} {message}")

def print_invalid2(mes, social_network, message, color=True):
    """Error output result verbose"""
    if color:
        print((Fore.RED + ".............[" +
            Style.BRIGHT + Fore.RED + "-" + Style.RESET_ALL +
            Fore.RED + "]" +
            Style.BRIGHT + Fore.GREEN + f" {social_network}:" +
            Style.RESET_ALL + Fore.YELLOW + f" {message}"))
    else:
        print(f"[-] {social_network} {message}")

def get_response(request_future, error_type, social_network, verbose=False, retry_no=None, color=True):
    try:
        rsp = request_future.result()
        if rsp.status_code:
            return rsp, error_type, rsp.elapsed
    except requests.exceptions.HTTPError as errh:
        print_error(errh, "HTTP Error:", social_network, verbose, color)

    except requests.exceptions.ConnectionError as errc:
        def gebb():
            global censor
            censor +=1
            print_error(errc, "Ошибка соединения:", social_network, verbose, color)
        gebb()            
    except requests.exceptions.Timeout as errt:
        print_error(errt, "Timeout ошибка:", social_network, verbose, color)
    except requests.exceptions.RequestException as err:
        print_error(err, "Keyboard layout error / * characters", social_network, verbose, color)
    return None, "", -1

def snoop(username, site_data, verbose=False, reports=False, user=False, country=False, print_found_only=False, timeout=None, color=True):
    username = re.sub(" ", "%20", username)

# Предотвращение 'DDoS' из-за невалидных логинов; номеров телефонов, ошибок поиска из-за спецсимволов.
    ermail=[]
    with open('domainlist.txt', 'r', encoding="utf-8") as err:
        for line in err.readlines():
            errdata=line[:-1]
            ermail.append(errdata)
    if any(ermail in username for ermail in ermail):
        print(Style.BRIGHT + Fore.RED + "\nE-mail the address will be shorten to a valid state")
        username = username.rsplit(sep='@', maxsplit=1)[0]

    with open('specialcharacters', 'r', encoding="utf-8") as errspec:
        s1 = errspec.read()
        my_list = list(s1)
        if any(my_list in username for my_list in my_list):
            print(Style.BRIGHT + Fore.RED + f"недопустимые символы в username: {username}")
            sys.exit(0)

    ernumber=['79', '89', "38", "37"]
    if any(ernumber in username[0:2] for ernumber in ernumber):
        if len(username) >= 10 and len(username) <= 13:
            if username.isdigit() == True:
                print(Style.BRIGHT + Fore.RED + "\nSnoop tracks user accounts, but not phone numbers...")
                sys.exit(0)
    elif username[0] == "+" or username[0] == ".":
        print (Style.BRIGHT + Fore.RED + "\nPublic login starting with such a character is almost always invalid...")
        sys.exit(0)
    elif username[0] == "9" and len(username) == 10 and username.isdigit() == True:
        print (Style.BRIGHT + Fore.RED + "\nSnoop tracks user accounts, but not phone numbers...")
        sys.exit(0)

# Печать первой инфостроки.
    if '%20' in username:
        usernameA = re.sub("%20", " ", username)
        print_info("looking for:", usernameA, color)
    else:
        print_info("wanted:", username, color)

# Создать сеанс на основе методологии запроса.
    underlying_session = requests.session()
    underlying_request = requests.Request()

# Рабочий лимит 20+
    try:
        if len(site_data) >= 50:
            max_workers=18
        else:
            max_workers=len(site_data)
    except:
        sys.exit(0)
# Создать многопоточный сеанс для всех запросов.
    session = ElapsedFuturesSession(max_workers=max_workers, session=underlying_session)

# Результаты анализа всех сайтов.
    results_total = {}

# Создание futures на все запросы. Это позволит распараллетить запросы.
    for social_network, net_info in site_data.items():
#        print([iz for iz in site_data]) #Тест вывода ключей (названия сайтов)
#        print(social_network) #(названия сайтов, строки)
# Результаты анализа конкретного сайта.
        results_site = {}

# Запись URL основного сайта и флага страные (сопоставление с data.json).
        results_site['flagcountry'] = net_info.get("country")
        results_site['flagcountryklas'] = net_info.get("country_klas")
        results_site['url_main'] = net_info.get("urlMain")

# Пользовательский user-agent браузера, некоторые сайты от этого зависят напрямую.
# Чтобы не думали, что запросы идут от ботов.

        RandHead = (["{'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}",
        "{'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}",
        "{'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36 OPR/60.0.3255.109'}",
        "{'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0'}"
        ])
        RH = random.choice(RandHead)
        headers = json.loads(RH.replace("'",'"'))

        if "headers" in net_info:
# Переопределить / добавить любые дополнительные заголовки, необходимые для данного сайта.
            headers.update(net_info["headers"])

# Не делать запрос, если имя пользователя не подходит для сайта.
        exclusionYES = net_info.get("exclusion")
        if exclusionYES and re.search(exclusionYES, username):
# Не нужно делать проверку на сайте: если это имя пользователя не допускается.
            if not print_found_only:
                print_invalid("", social_network, f"Invalid name format for this site", color)

            results_site["exists"] = "прочерк"
            results_site["url_user"] = ""
            results_site['countryCSV'] = ""
            results_site['http_status'] = ""
            results_site['response_text'] = ""
            results_site['check_time_ms'] = ""
            results_site['response_time_ms'] = ""
            results_site['response_time_site_ms'] = ""

        else:
# URL пользователя на сайте (если он существует).
            url = net_info["url"].format(username)
            results_site["url_user"] = url
            url_probe = net_info.get("urlProbe")
            if url_probe is None:
# URL-адрес — является обычным, который видят люди в Интернете.
                url_probe = url
            else:
# Существует специальный URL (обычно о нем мы не догадываемся/api) для проверки существования отдельно юзера.
                url_probe = url_probe.format(username)

# Если нужен только статус кода, не загружать код страницы.
            if reports:
                request_method = session.get
            else:
                try:
                    if net_info["errorTypе"] == 'status_code' or net_info["errorTypе"] == "redirection":
                        request_method = session.head
                    else:
                        request_method = session.get
                except:
                    sys.exit(0)
            if net_info["errorTypе"] == "response_url":
# Сайт перенаправляет запрос на другой URL, если имя пользователя не существует.
# Имя найдено. Запретить перенаправление чтобы захватить статус кода из первоначального url.
                allow_redirects = False
            else:
# Разрешить любой редирект, который хочет сделать сайт.
# Окончательным результатом запроса будет то, что доступно.
                allow_redirects = True

            future = request_method(url=url_probe, headers=headers, allow_redirects=allow_redirects, timeout=timeout)

# Сохранить future in data для последующего доступа.
            net_info["request_future"] = future

# Добавлять результаты этого сайта в окончательный словарь со всеми другими результатами.
        results_total[social_network] = results_site

# Открыть файл, содержащий ссылки на аккаунт.
# Основная логика: если текущие запросов, сделайте их. Если многопоточные запросы, дождаться ответов.

# print(results_site) # Проверка записи на успех.
    li_time = []
    if color == True and verbose == False:
        progress1 = Progress(BarColumn(bar_width=6),
        "[progress.percentage]{task.percentage:>3.0f}%", auto_refresh=False)
    else:
        progress1 = Progress(auto_refresh=False)
    if verbose == True:
        if color:
            progress1 = Progress(TimeRemainingColumn(),
            "[progress.percentage]{task.percentage:>3.0f}%", auto_refresh=False)
        else:
            progress1 = Progress(auto_refresh=False)

    for social_network, net_info in progress1.track(site_data.items(),description=""):
        if color:
            progress1.refresh()
# Получить результаты снова.
        results_site = results_total.get(social_network)

# Получить другую информацию сайта снова.
        url = results_site.get("url_user")
        countryA = results_site.get("flagcountry")
        countryB = results_site.get("flagcountryklas")
        exists = results_site.get("exists")
        if exists is not None:
            continue

# Получить ожидаемый тип данных 4 методов.
        error_type = net_info["errorTypе"]

# Данные по умолчанию в случае каких-либо сбоев в выполнении запроса.
        http_status = "*???"
        response_text = ""

# Получить future и убедиться, что оно закончено.
        future = net_info["request_future"]
        r, error_type, response_time = get_response(request_future=future,
                                                    error_type=error_type,
                                                    social_network=social_network,
                                                    verbose=verbose,
                                                    retry_no=3, 
                                                    color=color)

# Попытка получить информацию запроса.
        try:
            http_status =  r.status_code
        except:
            pass
        try:
            response_text = r.text.encode(r.encoding)
        except:
            pass

# Сохранение отчетов опция (-S)
        def sreports():
            codingWin = "charset=windows"
            codingWin2 = "charset=\"windows"
            try:
                os.makedirs(str(dirresults + f"/results/save reports/{username}"))
            except:
                pass
            if codingWin in r.text or codingWin2 in r.text:
                try:
                    with open(f"results/save reports/{username}/{social_network}.html", 'w',
                    encoding="cp1251") as rep:
                        rep.write(r.text)
                except:
                    with open(f"results/save reports/{username}/{social_network}.html", 'w',
                    encoding="utf-8") as rep:
                        rep.write(r.text)
            else:
                with open(f"results/save reports/{username}/{social_network}.html", 'w',
                encoding="utf-8") as rep:
                    rep.write(r.text)

# Проверка, 4 методов; #1.
# Ответы message (разные локации).
        if error_type == "message":
            error = net_info.get("errorMsg") 
            error2 = net_info.get("errorMsg2")
            if error2 in r.text:
                if not print_found_only:
                    print_not_found(social_network, response_time, verbose, color)
                exists = "увы"
            elif error in r.text:
                if not print_found_only:
                    print_not_found(social_network, response_time, verbose, color)
                exists = "увы"
            else:
                if sys.platform == 'win32':
                    print_found_country(social_network, url, countryB, response_time, verbose, color)
                else:
                    print_found_country(social_network, url, countryA, response_time, verbose, color)
                exists = "найден!"
                if reports:
                    sreports()
#            print(r.text) #Проверка ответа
# Проверка, 4 методов; #2.
# Проверка username при статусе 301 и 303 (перенаправление и соль).
        elif error_type == "redirection":
            rr = requests.get(url, allow_redirects=False)
            if rr.status_code == 301 or rr.status_code == 303:
#                print(r.text) #проверка ответа (+- '-S')
                if sys.platform == 'win32':
                    print_found_country(social_network, url, countryB, response_time, verbose, color)
                else:
                    print_found_country(social_network, url, countryA, response_time, verbose, color)
                if reports:
                    sreports()
                exists = "найден!"
            else:
                if not print_found_only:
                    print_not_found(social_network, response_time, verbose, color)
                exists = "oh :("

# Проверка, 4 методов; #3.
# Проверяет, является ли код состояния ответа 2..
        elif error_type == "status_code":
            if not r.status_code >= 300 or r.status_code < 200:
                if sys.platform == 'win32':
                    print_found_country(social_network, url, countryB, response_time, verbose, color)
                else:
                    print_found_country(social_network, url, countryA, response_time, verbose, color)
                if reports:
                    sreports()
                exists = "найден!"
            else:
                if not print_found_only:
                    print_not_found(social_network, response_time, verbose, color)
                exists = "увы"

# Проверка, 4 методов; #4
# Перенаправление.
        elif error_type == "response_url":

            if 200 <= r.status_code < 300:
                if sys.platform == 'win32':
                    print_found_country(social_network, url, countryB, response_time, verbose, color)
                else:
                    print_found_country(social_network, url, countryA, response_time, verbose, color)
                if reports:
                    sreports()
                exists = "found!"
            else:
                if not print_found_only:
                    print_not_found(social_network, response_time, verbose, color)
                exists = "oh :("
#            print(r.text) #Проверка ответа

# Если все 4 метода не сработали, например, из-за ошибки доступа (красный) или из-за каптчи (желтый)
        else:
            if not print_found_only and verbose == False:
                print_invalid("", social_network, "*PASS", color)
            elif not print_found_only and verbose == True:
                print_invalid2("", social_network, "*PASS", color)    
            exists = "block"

# Считать тайминги приближенно.
        ello = float(time.time() - timestart)
        li_time.append(ello)
        dif_time = []

# Считать тайминги с высокой точностью.
        try:
            time_site = str(response_time).rsplit(sep=':', maxsplit=1)[1]
            time_site=round(float(time_site)*1000)
        except:
            time_site = str("-")

        for i in (li_time[-2:-1]):
            i
            for i1 in (li_time[-1:]):
                i1
            dif = (i1-i)
            dif_time.append(dif)

# Опция '-v'.
            if verbose == True:
                if color == False:
                    if print_found_only == True:
                        if exists == "Found!" or exists == "block":
                            print(f"[*{time_site} ms ответ]" + \
                            f"────────────────────────────────────────[%.0f" % float(ello*1000) + " ms]")
                    else:
                        print(f"[*{time_site} ms response]" + \
                        f"────────────────────────────────────────[%.0f" % float(ello*1000) + " ms]")
                if color == True:
                    if print_found_only == True:
                        if exists == "Found!" or exists == "block":
                            if dif > 5:
                                print(Style.BRIGHT + Fore.RED + f"[**{time_site} ms response]"
                                f"────────────────────────────────────────[%.0f" % float(ello*1000) + " ms]")
                            else:
                                print(Style.BRIGHT + Fore.CYAN + f"[**{time_site} ms response]" + \
                                f"────────────────────────────────────────[%.0f" % float(ello*1000) + " ms]")
                    else:
                        if dif > 5:
                            print(Style.BRIGHT + Fore.RED + f"[**{time_site} ms response]" + \
                            f"────────────────────────────────────────[%.0f" % float(ello*1000) + " ms]")
                        else:
                            print(Style.BRIGHT + Fore.CYAN + f"[**{time_site} ms response]" + \
                            f"────────────────────────────────────────[%.0f" % float(ello*1000) + " ms]")

# Служебная информация для CSV.
        response_time_site_ms = 0
        for response_time_site_ms in dif_time:
            response_time_site_ms

# Сохранить сущ.флаг.
        results_site['exists'] = exists

# Сохранить результаты из запроса.
        results_site['countryCSV'] = countryB
        results_site['http_status'] = http_status
        results_site['response_text'] = response_text
        results_site['check_time_ms'] = time_site
        results_site['response_time_ms'] = round(float(ello*1000))
        if response_time_site_ms*1000 < 250:
            results_site['response_time_site_ms'] = "no"
        else:
            results_site['response_time_site_ms'] = round(float(response_time_site_ms*1000))
# Добавление результатов этого сайта в окончательный словарь со всеми другими результатами.
        results_total[social_network] = results_site
    return results_total


# Опция '-t'.
def timeout_check(value):
    try:
        global timeout
        timeout = int(value)
    except:
        raise ArgumentTypeError(f"\n\033[31;1mTimeout '{value}' Err,\033[0m \033[36indicate time in 'seconds'. \033[0m")
    if timeout <= 0:
        raise ArgumentTypeError(f"\033[31;1mTimeout '{value}' Err,\033[0m \033[36indicate time > 0sec. \033[0m")
    return timeout


# Обновление Snoop.
def update_snoop():
    if sys.platform == 'win32':
        upd = str(input("""Do you really want:
                    __             _  
   ._  _| _._|_ _  (_ ._  _  _ ._   ) 
|_||_)(_|(_| |_(/_ __)| |(_)(_)|_) o  
   |                           |    
enter 'y' """))
    else:
        upd = str(input("""\033[36mВы Do you want:
                    __             _  
   ._  _| _._|_ _  (_ ._  _  _ ._   ) 
|_||_)(_|(_| |_(/_ __)| |(_)(_)|_) o  
   |                           |    
enter\033[0m 'y' """))

    if upd == "y":
        if sys.platform == 'win32':
            print(Fore.RED + "Snoop update function requires installation <Git> на OS Windows")
            os.startfile("update.bat")
        else:
            print(Fore.RED + "Snoop update function requires installation <Git> на OS GNU/Linux")
            os.system("./update.sh")


# ОСНОВА.
def main():

# Запрос лицензии.
    with open('COPYRIGHT', 'r', encoding="utf8") as copyright:
        cop = copyright.read()

    version_snoop = f"\033[37m{cop}\033[0m\n" + \
                     f"\033[36m%(prog)s: {version}\033[36m\n" +  \
                     f"\033[36mOS: {platform.platform(aliased=True, terse=0)}\033[36m\n" + \
                     f"\033[36mPython: {platform.python_version()}\033[36m\n\n"
# Назначение опций Snoop.
    parser = ArgumentParser(formatter_class=RawDescriptionHelpFormatter,
                            description=f"{module_name} (Version {version})",
                            epilog=(Fore.CYAN + f"Snoop " + Style.BRIGHT + Fore.RED + f"Demo Version "+ Style.RESET_ALL + \
                            Fore.CYAN + f"поддержка: \033[31;1m{flagBS}\033[0m  \033[36mWebsites!\n"  + Fore.CYAN +
                            f"Snoop \033[36;1mFull Version\033[0m \033[36msupport: \033[36;1m1100+\033[0m \033[36mWebsites!!!\033[0m\n\n")
                            )
    parser.add_argument("--donate y", "-d y",
                        action="store_true", dest="donation",
                        help="Пожертвовать на развитие Snoop Project-а (получить \033[36mSnoop Full Version\033[0m)"
                        )
    parser.add_argument("--version", "--about", "-V",
                        action="version",  version=(version_snoop),
                        help="\033[31;1mНАЧАЛО! Вывод на печать версий: OS; Snoop; Python и Лицензии\033[0m"
                        )
    parser.add_argument("--verbose", "-v",
                        action="store_true",  dest="verbose", default=False,
                        help="Во время поиска 'username' выводить на печать подробную вербализацию"
                        )
    parser.add_argument("--base", "-b",
                        dest="json_file", default="BDdemo", metavar='',
                        help="Указать для поиска 'username' другую БД (Локально)/В demo version функция отключена"
                        )
    parser.add_argument("--web-base", "-w",
                        action="store_true", dest="web",
                        help="Подключиться для поиска 'username' к обновляемой web_БД (Online)"
                        )
    parser.add_argument("--site", "-s",
                        action="append", metavar='', 
                        dest="site_list",  default=None, 
                        help="Указать имя сайта из БД '--list all'. Поиск 'username' на одном указанном ресурсе"
                        )
    parser.add_argument("--time-out", "-t 9",
                        action="store", metavar='',
                        dest="timeout", type=timeout_check, default=5,
                        help="Установить выделение макс.времени на ожидание ответа от сервера (секунды).\n"
                             "Влияет на продолжительность поиска. Влияет на 'Timeout ошибки:'"
                             "\033[31;1mВкл. эту опцию необходимо практически всегда при медленном \
                             интернет соединении\033[0m, чтобы избежать длительных зависаний \
                             при неполадках в сети (по умолчанию значение выставлено 5с)" 
                        )
    parser.add_argument("--found-print", "-f", 
                        action="store_true", dest="print_found_only", default=False,
                        help="Выводить на печать только найденные аккаунты"
                        )
    parser.add_argument("--no-func", "-n",
                        action="store_true", dest="no_func", default=False,
                        help="""✓Монохромный терминал, не использовать цвета в url\n
                                ✓Отключить звук\n
                                ✓Запретить открытие web browser-а\n
                                ✓Отключить вывод на печать флагов стран
                                ✓Отключить индикацию и статус прогресса"""
                        )
    parser.add_argument("username",
                        nargs='+', metavar='USERNAMES',
                        action="store",
                        help="Никнейм разыскиваемого пользователя, поддерживается несколько имён"
                        )
    parser.add_argument("--userload", "-u", metavar='',
                        action="store", dest="user", default=False,
                        help="Указать файл со списком user-ов. Пример_Linux: 'python3 snoop.py -u ~/listusers.txt start'\n"
                             "Пример для Windows: 'python snoop.py -u c:\snoop\listusers.txt start'"
                        )                        
    parser.add_argument("--list all",
                        action="store_true", dest="listing",
                        help="Вывести на печать информацию о локальной базе данных Snoop"
                        )
    parser.add_argument("--country", "-c",
                        action="store_true", dest="country", default=False,
                        help="Сортировка 'вывода на печать/запись_результатов' по странам, а не по алфавиту"
                        )
    parser.add_argument("--save-report", "-S",
                        action="store_true", dest="reports", default=False,
                        help="Сохранять найденные странички пользователей в локальные файлы"
                        )
    parser.add_argument("--update y",
                        action="store_true", dest="update",
                        help="Обновить Snoop"
                        )

    args = parser.parse_args()

   
# Информативный вывод:
# Опция  '-w'.
    if args.web:
        print(Fore.CYAN + "[+] активирована опция '-w': «подключение к внешней web_database»")
# Опция  '-S'.
    if args.reports:
        print(Fore.CYAN + "[+] активирована опция '-S': «сохранять странички найденных аккаунтов»")

# Опция  '-n'.
    if args.no_func:
        print(Fore.CYAN + "[+] активирована опция '-n': «отключены:: цвета; звук; флаги; браузер; прогресс»")

# Опция  '-t'.
    try:
        if args.timeout:
            print(Fore.CYAN + f"[+] активирована опция '-t': «snoop будет ожидать ответа от сайта \033[36;1m<= {timeout}_sec\033[0m\033[36m.» \033[0m")
    except:
        pass

# Сортировка по странам '-с'.
    if args.country:
        patchjson = ("{}".format(args.json_file))
        jsonjson = fff()
        print(Fore.CYAN + "[+] активирована опция '-c': «сортировка/запись в HTML результатов по странам»")
        site_country = dict(jsonjson)
        country_sites = sorted(jsonjson, key=lambda k: ("country" not in k, jsonjson[k].get("country", sys.maxsize)))
        sortC = {}
        for site in country_sites:
            sortC[site] = site_country.get(site)

# Опция '-f'.
    if args.print_found_only:
        print(Fore.CYAN + "[+] активирована опция '-f': «выводить на печать только найденные аккаунты»")

# Опция '-s'.
    if args.site_list:
        print(Fore.CYAN + "[+] активирована опция '-s': «будет произведён поиск user-a на 1-м выбранном website»\n"
        "    допустимо использовать опцию '-s' несколько раз\n"
        "    опция '-s' несовместима с опцией '-с'")        

# Опция '-v'
    if args.verbose:
        print(Fore.CYAN + "[+] активирована опция '-v': «подробная вербализация в CLI»")
        networktest.nettest()


# Опция '--list all'.
    if args.listing:
        from rich.console import Console
        from rich.table import Table

        if sys.platform == 'win32':
            sortY = str(input("Сортировать БС Snoop по странам, по имени сайта или обобщенно ?\nпо странам — 1 по имени — 2 all — 3\n"))
        else:
            sortY = str(input("\033[36mСортировать БС Snoop по странам, по имени сайта или обобщенно ?\n" + \
            "по странам —\033[0m 1 \033[36mпо имени —\033[0m 2 \033[36mall —\033[0m 3\n" + \
            "\033[36mВыберите действие...\033[0m\n"))
# Общий вывод стран (3!).
        if sortY == "3":
            print(Fore.CYAN + "========================\nOk, print All Country:\n")
            datajson0 = fff()
            cnt0 = Counter()
            li0 = []
            for con0 in datajson0:
                if sys.platform == 'win32':
                    aaa0 = datajson0.get(con0).get("country_klas")
                else:
                    aaa0 = datajson0.get(con0).get("country")
                li0.append(aaa0)
            for word0 in li0:
                cnt0[word0] += 1
            flag_str0=str(cnt0)
            try:
                flag_str_sum0 = (flag_str0.split('{')[1]).replace("'", "").replace("}", "").replace(")", "")
            except:
                pass
            table = Table(title = Style.BRIGHT + Fore.RED + "Snoop Demo Version" + Style.RESET_ALL, style="green")
            table.add_column("Страна:Кол-во websites", style="magenta")
            table.add_column("All", style="cyan", justify='full')
            table.add_row(flag_str_sum0, str(len(datajson0)))
            console = Console()
            console.print(table)
# Вывод для full Version
            datajson00 = kkk()
            cnt00 = Counter()
            li00 = []
            for con00 in datajson00:
                if sys.platform == 'win32':
                    aaa00 = datajson00.get(con00).get("country_klas")
                else:
                    aaa00 = datajson00.get(con00).get("country")
                li00.append(aaa00)
            for word00 in li00:
                cnt00[word00] += 1
            flag_str00=str(cnt00)
            try:
                flag_str_sum00 = (flag_str00.split('{')[1]).replace("'", "").replace("}", "").replace(")", "")
            except:
                pass
            table = Table(title = Style.BRIGHT + Fore.GREEN + "Snoop Full Version" + Style.RESET_ALL, style="green")
            table.add_column("Страна:Кол-во websites", style="magenta")
            table.add_column("All", style="cyan", justify='full')
            table.add_row(flag_str_sum00, str(len(datajson00)))
            console = Console()
            console.print(table)
            sys.exit(0)

# Сортируем по алфавиту (2!).
# Сортировка для ОС Win Full Version.
        elif sortY == "2":
            print(Fore.CYAN + "========================\nOk, сортируем по алфавиту:\n")
            print(Fore.GREEN + "++Белый список Full Version++")
            datajson = kkk()
            i = 0
            if sys.platform == 'win32':
                for con in datajson:
                    aaa = datajson.get(con).get("country_klas")
                    i += 1
                    print(Style.BRIGHT + Fore.GREEN + f"{i}.", Fore.CYAN + f"{aaa}  {con}")
                    print(Fore.CYAN + "================")
# Сортировка для ОС GNU Full Version..
            else:
                for con in datajson:
                    aaa = datajson.get(con).get("country")
                    i += 1
                    print(Style.BRIGHT + Fore.GREEN + f"{i}.", Fore.CYAN + f"{aaa}  {con}")
                    print(Fore.CYAN + "================")        
# Сортировка для ОС Win Demo Version.
            print(Fore.GREEN + "\n++Белый список Demo Version++")
            datajson = fff()
            i = 0
            if sys.platform == 'win32':
                for con in datajson:
                    aaa = datajson.get(con).get("country_klas")
                    i += 1
                    print(Style.BRIGHT + Fore.GREEN + f"{i}.", Fore.CYAN + f"{aaa}  {con}")
                    print(Fore.CYAN + "================")
# Сортировка для ОС GNU Demo Version.
            else:
                for con in datajson:
                    aaa = datajson.get(con).get("country")
                    i += 1
                    print(Style.BRIGHT + Fore.GREEN + f"{i}.", Fore.CYAN + f"{aaa}  {con}")
                    print(Fore.CYAN + "================")        
            sys.exit(0)

# Сортируем по странам (1!).
# Сортировка для ОС Win Full Version.
        elif sortY == "1":
            if sys.platform == 'win32':
                listwindows = []
                datajson = kkk()
                for con in datajson:
                    aaa = (datajson.get(con).get("country_klas"))
                    listwindows.append(f"{aaa}  {con}\n")
                sort_spisok=sorted(listwindows)
                print(Fore.CYAN + "========================\nOk, сортируем по странам:\n")
                print(Fore.GREEN + "++Белый список Full Version++")
                for i, numerlist in enumerate(sort_spisok):
                    i += 1
                    print(Style.BRIGHT + Fore.GREEN + f"{i}.", Fore.CYAN + f"{numerlist}",end = '')
                    print(Fore.CYAN + "================") 
# Сортировка для ОС GNU Full Version.
            else:
                listlinux = []
                datajson = kkk()
                for con in datajson:
                    aaa = (datajson.get(con).get("country"))
                    listlinux.append(f"{aaa}  {con}\n")
                sort_spisok=sorted(listlinux)
                print(Fore.CYAN + "========================\nOk, сортируем по странам:\n")
                print(Fore.GREEN + "++Белый список Full Version++")
                for i, numerlist in enumerate(sort_spisok):
                    i += 1
                    print(Style.BRIGHT + Fore.GREEN + f"{i}.", Fore.CYAN + f"{numerlist}",end = '')
                    print(Fore.CYAN + "================") 
# Сортировка для ОС Win Demo Version.
            if sys.platform == 'win32':
                listwindows = []
                datajson = fff()
                for con in datajson:
                    aaa = (datajson.get(con).get("country_klas"))
                    listwindows.append(f"{aaa}  {con}\n")
                sort_spisok=sorted(listwindows)
                print(Fore.GREEN + "\n++Белый список Demo Version++")
                for i, numerlist in enumerate(sort_spisok):
                    i += 1
                    print(Style.BRIGHT + Fore.GREEN + f"{i}.", Fore.CYAN + f"{numerlist}",end = '')
                    print(Fore.CYAN + "================") 
# Сортировка для ОС GNU Demo Version..
            else:
                listlinux = []
                datajson = fff()
                for con in datajson:
                    aaa = (datajson.get(con).get("country"))
                    listlinux.append(f"{aaa}  {con}\n")
                sort_spisok=sorted(listlinux)
                print(Fore.GREEN + "\n++Белый список Demo Version++")
                for i, numerlist in enumerate(sort_spisok):
                    i += 1
                    print(Style.BRIGHT + Fore.GREEN + f"{i}.", Fore.CYAN + f"{numerlist}",end = '')
                    print(Fore.CYAN + "================") 
            sys.exit(0)
# Действие не выбрано.
        else:
            print(Style.BRIGHT + Fore.RED + "Извините, но вы не выбрали действие\nвыход")
            sys.exit(0)

# Опция донат '-d y'.
    if args.donation:
        print(donate)
        print("                                                                              ||\n",
              Fore.CYAN + f"Ограничения Demo Version: {flagBS} Websites (Database Snoop сокращена в > 19 раз); ||\n"
              f"отключены некоторые опции; необновляемая и не поддерживаемая Database_Snoop.  ||\n"
              f"Snoop Full Version: 1100+ Websites; поддержка и обновление Database Snoop.    ||\n"
	      	  f"\033[36;1mПодключение к Web_Database Snoop (online), которая расширяется/обновляется.   ||\033[0m\n"
              f"===============================================================================\n")
        webbrowser.open("https://yasobe.ru/na/snoop_project")
        print(Style.BRIGHT + Fore.RED + "Выход")
        sys.exit(0)

# Опция указания файла-списка разыскиваемых пользователей '-u'.
    if args.user:
        userlist = []
        patchuserlist = ("{}".format(args.user))
        userfile=patchuserlist.split('/')[-1]
        with open(patchuserlist, "r", encoding="utf8") as u1:
            try:
                for lineuserlist in u1.readlines():
                    lineuserlist.strip()
                    userlist.append(lineuserlist)
                userlist=[line.rstrip() for line in userlist]
            except:
                print("\033[31;1mНе могу найти_прочитать!\033[0m \033[36mПожалуйста, укажите текстовый файл в кодировке —\033[0m \033[36;1mutf-8.\033[0m\n")
                print("\033[36mПо умолчанию блокнот в OS Windows сохраняет текст в кодировке — ANSI\033[0m")
                print("\033[36mОткройте ваш список пользователей и измените кодировку [файл ---> сохранить как ---> utf-8]")
                print("\033[36mИли удалите из словаря нечитаемые символы.")
                sys.exit(0)
        print(Fore.CYAN + f"[+] активирована опция '-u': «розыск user-ов из файла: \033[36;1m{userfile}\033[0m\033[36m»\033[0m")
        print(Fore.CYAN + "    Будем искать:" + f" {userlist[:3]}" + " и других..." + Style.RESET_ALL)

# Завершение обновления Snoop.
    if args.update:
        print("\033[36m=======================\033[0m")
        update_snoop()
        print("\033[36m=======================\n", Style.BRIGHT + Fore.RED +"\nВыход")
        sys.exit(0)

# Проверка остальных опций.
    response_json_online = None
    site_data_all = None

    baseput = ("{}".format(args.json_file))
#    print(baseput) #проверка пути базы

# Работа с базой.
    if site_data_all is None:
# Проверить, существует ли альтернативная база данных, иначе выход.
        if not os.path.exists(baseput):
            print("\033[31;1mФайла базы не существует.\033[0m")
            sys.exit(0)
        else:
            try:
                a1 = fff()
            except:
                print("\033[31;1mНеподдерживаемый формат базы данных\033[0m")
        try:
            if args.web == False:
                site_data_all = a1
                print(Fore.CYAN + f"\nзагружена локальная база: " + 
                Style.BRIGHT + Fore.CYAN + f"{len(site_data_all)}" + "_Websites" + Style.RESET_ALL)
        except:
            print("\033[31;1mInvalid загружаемая база данных.\033[0m")

# Опция '-w'
    if args.web:
        print("\n\033[37m\033[44m{}".format("Функция действует только для пользователей Full version..."))
        print(donate)
        print("\033[31mВыход\033[0m")
        webbrowser.open("https://yasobe.ru/na/snoop_project")
        sys.exit(0)

    if args.site_list is None:
# Не желательно смотреть на подмножество сайтов.
        site_data = site_data_all
    else:

# Опция '-s'.
# Пользователь желает выборочно запускать запросы к подмножеству списку сайтов.
# Убедиться, что сайты поддерживаются, создать сокращенную базу данных сайта.
        site_data = {}
        site_missing = []
        for site in args.site_list:
            for existing_site in site_data_all:
                if site.lower() == existing_site.lower():
                    site_data[existing_site] = site_data_all[existing_site]
            if not site_data:

# Создать список сайтов, которые не поддерживаются, для будущего сообщения об ошибке.
                site_missing.append(f"'{site}'")

        if site_missing:
            print(
                f"\033[31;1mОшибка:\033[0m \033[36mжелаемый сайт не найден в базе Snoop:: {', '.join(site_missing)}\033[0m")
            sys.exit(0)

# Запуск с опцией '-u' (получаем 'username' из файла).
# Крутим список юзеров.
    if args.user:
        kef_user=0
        for username in userlist:
            kef_user +=1
            file = open("results/txt/" + username + ".txt", "w", encoding="utf-8")
            try:
                file = open("results/txt/" + username + ".txt", "w", encoding="utf-8")
            except (SyntaxError, ValueError):
                pass

            try:
                if args.country ==True:
                    results = snoop(username,
                                   sortC,
                                   country=args.country,
                                   user=args.user,
                                   verbose=args.verbose,
                                   reports=args.reports,
                                   print_found_only=args.print_found_only,
                                   timeout=args.timeout,
                                   color=not args.no_func)
                else:
                    results = snoop(username,
                                   site_data,
                                   country=args.country,
                                   user=args.user,
                                   verbose=args.verbose,
                                   reports=args.reports,
                                   print_found_only=args.print_found_only,
                                   timeout=args.timeout,
                                   color=not args.no_func)
            except:
                results = snoop(username,
                               site_data,
                               country=args.country,
                               user=args.user,
                               verbose=args.verbose,
                               reports=args.reports,
                               print_found_only=args.print_found_only,
                               timeout=args.timeout,
                               color=not args.no_func)

            exists_counter = 0
            file.write("Адрес | ресурс" + "\n\n")
            for website_name in results:
                timefinish = time.time() - timestart            
                dictionary = results[website_name]
                if dictionary.get("exists") == "найден!":
                    exists_counter += 1
                    file.write(dictionary ["url_user"] + " | " + (website_name)+"\n")
            file.write("\n" f"Запрашиваемый объект: <{username}> найден: {exists_counter} раз(а).")
            file.write("\n" f"База Snoop (DemoVersion): " + str(flagBS) + " Websites.")
            file.write("\n" f"Обновлено: " + time.strftime("%d/%m/%Y_%H:%M:%S", time_data) + ".")      
            print(Fore.CYAN + "├─Результаты поиска:", "найдено -->", exists_counter, "url (%.0f" % float(timefinish) +"sec)")
            print(Fore.CYAN + "├──Результаты сохранены в: " + Style.RESET_ALL + "results/*/" + str(username) + ".*")

    # Запись в html.
            file = open("results/html/" + username + ".html", "w", encoding="utf-8")
            try:
                file = open("results/html/" + username + ".html", "w", encoding="utf-8")
            except (SyntaxError, ValueError):
                pass
            file.write("<!DOCTYPE html>\n<head>\n<meta charset='utf-8'>\n<style>\nbody { background: url(../../web/public.png) \
            no-repeat 20% 0%; }\n</style>\n<link rel='stylesheet' href='../../web/style.css'>\n</head>\n<body>\n\n\
            <div id='particles-js'></div>\n\
            <div id='report'>\n\n\
            <h1><a class='GL' href='file://" + str(dirresults) + "/results/html/'>Главная</a>" + "</h1>\n")
            file.write("""\t\t\t<h3>Snoop Project (Demo Version)</h3>
            <p>Нажмите: 'сортировать по странам', возврат: 'F5':</p>
            <button onclick="sortList()">Сортировать по странам</button><br><br>\n\n""")
            file.write("Объект " + "<b>" + (username) + "</b>" + " найден на нижеперечисленных " + "<b>" + str(exists_counter) + 
            "</b> ресурсах:\n" + "<br><ol" + " id='id777'>\n")
            
            cnt = Counter()
            for website_name in results:
                dictionary = results[website_name]
                flag_sum=dictionary["flagcountry"]
                if dictionary.get("exists") == "найден!":
                    li = []
                    li.append(flag_sum)
                    exists_counter += 0
                    for word in li:
                        cnt[word] += 1
                    file.write("<li>" + dictionary["flagcountry"]+ "<a target='_blank' href='" + dictionary ["url_user"] + "'>"+ 
                    (website_name) + "</a>" + "</li>\n")
            flag_str=str(cnt)
            try:            
                flag_str_sum = (flag_str.split('{')[1]).replace("'", "").replace("}", "").replace(")", "").replace(",", "  ↯  ").replace(":", "⇔")
                file.write("</ol>GEO: " + str(flag_str_sum) + ".\n")
            except:
                pass
            file.write("<br> Запрашиваемый объект < <b>" + str(username) + "</b> > найден: <b>" + str(exists_counter) + "</b> раз(а).")
            file.write("<br> Затраченное время на создание отчёта: " + "<b>" + "%.0f" % float(timefinish) + "</b>" + " c.\n")
            file.write("<br> База Snoop (DemoVersion): <b>" + str(flagBS) + "</b>" + " Websites.\n")
            file.write("<br> Обновлено: " + "<i>" + time.strftime("%d/%m/%Y_%H:%M:%S", time_data) + ".</i><br><br>\n")
            file.write("""
    <script>
    function sortList() {
      var list, i, switching, b, shouldSwitch;
      list = document.getElementById('id777');
      switching = true;
      while (switching) {
        switching = false;
        b = list.getElementsByTagName("LI");
        for (i = 0; i < (b.length - 1); i++) {
          shouldSwitch = false;
          if (b[i].innerHTML.toLowerCase() > b[i + 1].innerHTML.toLowerCase()) {
            shouldSwitch = true;
            break;
          }
        }
        if (shouldSwitch) {
          b[i].parentNode.insertBefore(b[i + 1], b[i]);
          switching = true;
        }
      }
    }
    </script>

<script src="../../web/particles.js"></script>
<script src="../../web/app.js"></script>

<audio controls="controls" autoplay="autoplay" loop="loop">
<source src="../../web/Megapolis (remix).mp3" type="audio/mpeg">
</audio>

<br>
<audio controls="controls" loop="loop">
<source src="../../web/for snoop in cyberpunk.mp3" type="audio/mpeg">
</audio>

<br><br>

<a target='_blank' href='https://github.com/snooppr/snoop' class="SnA"><span class="SnSpan">💊 Source Исходный код</span></a>
<a target='_blank' href='https://yasobe.ru/na/snoop_project' class="DnA"><span class="DnSpan">💊 Donation Пожертвование</span></a>
<br><br><br><br>

</body>
</html>""")
            file.close()

    # Запись в csv.
            with open("results/csv/" + username + ".csv", "w", newline='', encoding="utf-8") as csv_report:
                usernamsCSV = re.sub(" ", "_", username)
                if censor >= 11 * int(kef_user):
                    writer = csv.writer(csv_report)
                    writer.writerow(['Объект',
                                     'Ресурс',
                                     'Стана',
                                     'Url',
                                     'Url_username',
                                     'Статус',
                                     'Статус_http',
                                     'Общее_замедление/мс',
                                     'Отклик/мс',
                                     'Общее_время/мс',
                                     'Внимание!_Поиск_проходил_при_нестабильном_интернет_соединении_или_Internet-Censorship. '
                                     'Результаты_могут_быть_неполные.'
                                     ])
                else:
                    writer = csv.writer(csv_report)
                    writer.writerow(['Объект',
                                     'Ресурс',
                                     'Стана',
                                     'Url',
                                     'Url_username',
                                     'Статус',
                                     'Статус_http',
                                     'Общее_замедление/мс',
                                     'Отклик/мс',
                                     'Общее_время/мс'
                                     ])
                for site in results:
                    writer.writerow([usernamsCSV,
                                     site,
                                     results[site]['countryCSV'],
                                     results[site]['url_main'],
                                     results[site]['url_user'],
                                     results[site]['exists'],
                                     results[site]['http_status'],
                                     results[site]['response_time_site_ms'],
                                     results[site]['check_time_ms'],
                                     results[site]['response_time_ms']
                                     ])
                writer.writerow(['«---------------------------------------',
                                 '--------','----', '----------------------------------',
                                 '--------------------------------------------------------',
                                 '-------------', '-----------------', '--------------------------------', 
                                 '-------------', '-----------------------»'])
                writer.writerow(['База_Snoop(DemoVersion)=' + str(flagBS) + '_Websites'])
                writer.writerow('')
                writer.writerow(['Дата'])
                writer.writerow([time.strftime("%d/%m/%Y_%H:%M:%S", time_data)])
                file.close()

    # Финишный вывод.
        if censor >= 11 * int(kef_user):
            print(Fore.CYAN + "├───Дата поискового запроса:", time.strftime("%d/%m/%Y_%H:%M:%S", time_data))
            print(Fore.CYAN + "└────\033[31;1mВнимание!\033[0m", Fore.CYAN + "Нестабильное соединение или Internet Censorship:", 
                              "*используйте VPN")
            print("\n\033[37m\033[44m{}".format("Лицензия: авторская"))
        else:
            print(Fore.CYAN + "└───Дата поискового запроса:", time.strftime("%d/%m/%Y_%H:%M:%S", time_data))
            print("\n\033[37m\033[44m{}".format("Лицензия: авторская"))

# Поиск по умолчанию (без опции '-u').
    else:
        for username in args.username:
            
            file = open("results/txt/" + username + ".txt", "w", encoding="utf-8")
            try:
                file = open("results/txt/" + username + ".txt", "w", encoding="utf-8")
            except (SyntaxError, ValueError):
                pass

            try:
                if args.country ==True:
                    results = snoop(username,
                                   sortC,
                                   country=args.country,
                                   user=args.user,
                                   verbose=args.verbose,
                                   reports=args.reports,
                                   print_found_only=args.print_found_only,
                                   timeout=args.timeout,
                                   color=not args.no_func)
                else:
                    results = snoop(username,
                                   site_data,
                                   country=args.country,
                                   user=args.user,
                                   verbose=args.verbose,
                                   reports=args.reports,
                                   print_found_only=args.print_found_only,
                                   timeout=args.timeout,
                                   color=not args.no_func)
            except:
                results = snoop(username,
                               site_data,
                               country=args.country,
                               user=args.user,
                               verbose=args.verbose,
                               reports=args.reports,
                               print_found_only=args.print_found_only,
                               timeout=args.timeout,
                               color=not args.no_func)
            exists_counter = 0
            file.write("Адрес | ресурс" + "\n\n")
            for website_name in results:
                timefinish = time.time() - timestart            
                dictionary = results[website_name]
                if dictionary.get("exists") == "найден!":
                    exists_counter += 1
                    file.write(dictionary ["url_user"] + " | " + (website_name)+"\n")
            file.write("\n" f"Запрашиваемый объект: <{username}> найден: {exists_counter} раз(а).")
            file.write("\n" f"База Snoop (DemoVersion): " + str(flagBS) + " Websites.")
            file.write("\n" f"Обновлено: " + time.strftime("%d/%m/%Y_%H:%M:%S", time_data) + ".")
            print(Fore.CYAN + "├─Результаты поиска:", "найдено -->", exists_counter, "url (%.0f" % float(timefinish) +"sec)")
            print(Fore.CYAN + "├──Результаты сохранены в: " + Style.RESET_ALL + "results/*/" + str(username) + ".*")


    # Запись в html.
            file = open("results/html/" + username + ".html", "w", encoding="utf-8")
            try:
                file = open("results/html/" + username + ".html", "w", encoding="utf-8")
            except (SyntaxError, ValueError):
                pass
            file.write("<!DOCTYPE html>\n<head>\n<meta charset='utf-8'>\n<style>\nbody { background: url(../../web/public.png) \
            no-repeat 20% 0%; }\n</style>\n<link rel='stylesheet' href='../../web/style.css'>\n</head>\n<body>\n\n\
            <div id='particles-js'></div>\n\
            <div id='report'>\n\n\
            <h1><a class='GL' href='file://" + str(dirresults) + "/results/html/'>Главная</a>" + "</h1>\n")
            file.write("""\t\t\t<h3>Snoop Project (Demo Version)</h3>
            <p>Нажмите: 'сортировать по странам', возврат: 'F5':</p>
            <button onclick="sortList()">Сортировать по странам</button><br><br>\n\n""")
            file.write("Объект " + "<b>" + (username) + "</b>" + " найден на нижеперечисленных " + "<b>" + str(exists_counter) + 
            "</b> ресурсах:\n" + "<br><ol" + " id='id777'>\n")
            
            cnt = Counter()
            for website_name in results:
                dictionary = results[website_name]
                flag_sum=dictionary["flagcountry"]
                if dictionary.get("exists") == "найден!":
                    li = []
                    li.append(flag_sum)
                    exists_counter += 0
                    for word in li:
                        cnt[word] += 1
                    file.write("<li>" + dictionary["flagcountry"]+ "<a target='_blank' href='" + dictionary ["url_user"] + "'>"+ 
                    (website_name) + "</a>" + "</li>\n")
            flag_str=str(cnt)
            try:            
                flag_str_sum = (flag_str.split('{')[1]).replace("'", "").replace("}", "").replace(")", "").replace(",", "  ↯  ").replace(":", "⇔")
                file.write("</ol>GEO: " + str(flag_str_sum) + ".\n")
            except:
                pass
            file.write("<br> Запрашиваемый объект < <b>" + str(username) + "</b> > найден: <b>" + str(exists_counter) + "</b> раз(а).")
            file.write("<br> Затраченное время на создание отчёта: " + "<b>" + "%.0f" % float(timefinish) + "</b>" + " c.\n")
            file.write("<br> База Snoop (DemoVersion): <b>" + str(flagBS) + "</b>" + " Websites.\n")
            file.write("<br> Обновлено: " + "<i>" + time.strftime("%d/%m/%Y_%H:%M:%S", time_data) + ".</i><br><br>\n")
            file.write("""
    <script>
    function sortList() {
      var list, i, switching, b, shouldSwitch;
      list = document.getElementById('id777');
      switching = true;
      while (switching) {
        switching = false;
        b = list.getElementsByTagName("LI");
        for (i = 0; i < (b.length - 1); i++) {
          shouldSwitch = false;
          if (b[i].innerHTML.toLowerCase() > b[i + 1].innerHTML.toLowerCase()) {
            shouldSwitch = true;
            break;
          }
        }
        if (shouldSwitch) {
          b[i].parentNode.insertBefore(b[i + 1], b[i]);
          switching = true;
        }
      }
    }
    </script>

<script src="../../web/particles.js"></script>
<script src="../../web/app.js"></script>

<audio controls="controls" autoplay="autoplay" loop="loop">
<source src="../../web/Megapolis (remix).mp3" type="audio/mpeg">
</audio>

<br>
<audio controls="controls" loop="loop">
<source src="../../web/for snoop in cyberpunk.mp3" type="audio/mpeg">
</audio>

<br><br>

<a target='_blank' href='https://github.com/snooppr/snoop' class="SnA"><span class="SnSpan">💊 Source Исходный код</span></a>
<a target='_blank' href='https://yasobe.ru/na/snoop_project' class="DnA"><span class="DnSpan">💊 Donation Пожертвование</span></a>
<br><br><br><br>

</body>
</html>""")
            file.close()

    # Запись в csv.
            with open("results/csv/" + username + ".csv", "w", newline='', encoding="utf-8") as csv_report:
                usernamCSV = re.sub(" ", "_", username)

                if censor >= 11:            
                    writer = csv.writer(csv_report)
                    writer.writerow(['Объект',
                                     'Ресурс',
                                     'Стана',
                                     'Url',
                                     'Url_username',
                                     'Статус',
                                     'Статус_http',
                                     'Общее_замедление/мс',
                                     'Отклик/мс',
                                     'Общее_время/мс',
                                     'Внимание!_Поиск_проходил_при_нестабильном_интернет_соединении_или_Internet-Censorship. '
                                     'Результаты_могут_быть_неполные.'
                                     ])
                else:
                    writer = csv.writer(csv_report)
                    writer.writerow(['Объект',
                                     'Ресурс',
                                     'Стана',
                                     'Url',
                                     'Url_username',
                                     'Статус',
                                     'Статус_http',
                                     'Общее_замедление/мс',
                                     'Отклик/мс',
                                     'Общее_время/мс'
                                     ])
                for site in results:
                    writer.writerow([usernamCSV,
                                     site,
                                     results[site]['countryCSV'],
                                     results[site]['url_main'],
                                     results[site]['url_user'],
                                     results[site]['exists'],
                                     results[site]['http_status'],
                                     results[site]['response_time_site_ms'],
                                     results[site]['check_time_ms'],
                                     results[site]['response_time_ms']
                                     ])
                writer.writerow(['«---------------------------------------',
                                 '--------','----', '----------------------------------',
                                 '--------------------------------------------------------',
                                 '-------------', '-----------------', '--------------------------------',
                                 '-------------', '-----------------------»'])
                writer.writerow(['База_Snoop(DemoVersion)=' + str(flagBS) + '_Websites'])
                writer.writerow('')
                writer.writerow(['Дата'])
                writer.writerow([time.strftime("%d/%m/%Y_%H:%M:%S", time_data)])
                file.close()

    # Финишный вывод.
        if censor >= 11:
            print(Fore.CYAN + "├───Дата поискового запроса:", time.strftime("%d/%m/%Y_%H:%M:%S", time_data))
            print(Fore.CYAN + "└────\033[31;1mВнимание!\033[0m", Fore.CYAN + "Нестабильное соединение или Internet Censorship:", "*используйте VPN")
            print("\n\033[37m\033[44m{}".format("Лицензия: авторская"))
        else:
            print(Fore.CYAN + "└───Дата поискового запроса:", time.strftime("%d/%m/%Y_%H:%M:%S", time_data))
            print("\n\033[37m\033[44m{}".format("Лицензия: авторская"))

# Открывать/нет браузер с результатами поиска.
    if args.no_func==False:
        if exists_counter >= 1:
            webbrowser.open(str("file://" + str(dirresults) + "/results/html/" + str(username) + ".html"))
# Музыка.
        try:
            playsound('end.wav')
        except:
            pass

if __name__ == "__main__":
    main()
