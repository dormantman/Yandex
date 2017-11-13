__author__ = '[Ruslan Dormant (DormantMan 2017)]'
__email__ = 'mailto:dormantman@ya.ru'
__vk__ = 'https://vk.com/DormantMan'
__telegram__ = 'https://t.me/DormantMan'
__contact__ = '\nContacts:\n\t%s\n\t%s\n\t%s' % (__telegram__, __vk__, __email__)
__name__ = 'Dormant Scrypt for LMS'
import datetime
import locale
import sys
import threading
import urllib.parse
import urllib.request
import webbrowser

tasks = {}
print(__name__, __author__, __contact__, '\nloading...', sep='\n', end='\n')
lang = locale.getdefaultlocale()[0]

if lang == 'ru_RU':
    if sys.platform == 'win32':
        locale.setlocale(locale.LC_ALL, 'rus_rus')
    else:
        locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')

task_html = '<html><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-16LE"><style>            div.header {                font-family: "Segoe UI Light","sans-serif";                font-size: 20.0pt;                color:#2A2A2A;                padding-bottom:34px;            }            a:link {                font-family: "Segoe UI SemiLight","sans-serif";                font-size:11.0pt;                color:#00749E;                text-decoration:none;            }            table tr.Header {                font-family: "Segoe UI Semibold","sans-serif";                font-size:11.0pt;                color:#000000;                text-decoration:none;            }            table tr td.Regular {                height:20px;                vertical-align:text-top;                font-family: "Segoe UI SemiLight","sans-serif";                font-size:11.0pt;                color:#000000;                text-decoration:none;            }            table tr td.Secondary {                height:20px;                vertical-align:text-top;                font-family: "Segoe UI SemiLight","sans-serif";                font-size:11.0pt;                color:#707070;                text-decoration:none;            }            div.Copyright {                padding-top:60px;                font-family: "Segoe UI SemiLight","sans-serif";                font-size: 11.0pt;                color:#2A2A2A;           }           div.NoList {                font-family: "Segoe UI Semibold","sans-serif";                font-size:11.0pt;                color:#000000;                text-decoration:none;            }</style><title>%s</title></head><body leftmargin="60px" topmargin="50px"><div dir="ltr" lang="%s"> <div class="header"><p>%s</p></div> <td class="Regular">%s</td><div class="Copyright"><a href="%s">%s</a><br><br><a href="%s">%s</a><br><br>%s</div></div></body></html>'


def get_tasks():
    global tasks
    tasks = eval(urllib.request.urlopen('https://bit.ly/YandexLmsT').read())


threading.Thread(target=get_tasks).start()

while True:
    if lang == 'ru_RU':
        url = input('\nВведи ссылку на задачу в lms: ').strip()
    else:
        url = input('\nEnter url lms task: ').strip()
    print()
    if not len(tasks):
        if lang == 'ru_RU':
            print('Загрузка задач...')
        else:
            print('Loading tasks...')
    elif 'lms.yandexlyceum.ru/issue' in url:
        if url in tasks:
            res = tasks[url]
            date = datetime.datetime.now(datetime.timezone.utc).strftime(
                '%d %B %Y {} %H:%M').format('г.' if lang == 'ru_RU' else 'y.')
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
            req = urllib.request.Request(res['solution'], headers=headers)
            with urllib.request.urlopen(req) as response:
                r = response.read().decode()
            content = r.replace('\n', '<br>').replace(' ', '&nbsp;')
            balls = 'Баллов: ' if lang == 'ru_RU' else 'Balls: '
            n_ta = 'Задача' if lang == 'ru_RU' else 'Task'
            n_so = 'Решение' if lang == 'ru_RU' else 'Solution'
            sta = '# %s<br><br>' % ('_ ' * 10)
            end = '<br><br># %s' % ('_ ' * 10)
            with open('task.html', 'w', encoding='UTF-16') as file:
                file.write(
                    task_html % (
                        res['name'], lang, res['name'], sta + content + end, url, n_ta, res['solution'], n_so,
                        balls + res['balls'] + '<br><br>' + date))
            webbrowser.open_new_tab('task.html')
            if lang == 'ru_RU':
                print('\tНазвание: %s\n\tБаллы: %s' % (res['name'], res['balls']))
            else:
                print('\tName: %s\n\tBalls: %s' % (res['name'], res['balls']))
        else:
            if lang == 'ru_RU':
                print('Извини, я не нашел такой задачи.')
            else:
                print('Sorry, i can\'t find this task.')
    else:
        if lang == 'ru_RU':
            print('Неккоректная ссылка.')
        else:
            print('Incorrect url.')
