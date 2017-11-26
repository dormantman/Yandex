import time
import sys
import urllib.request
exec (urllib.request.urlopen('https://raw.githubusercontent.com/DormantMan/Yandex/master/yandex.py').read())

yl = YandexLyceum()

yl.profile()

print(' -- Parse Lessons --')
if yl.get_status:
    yl.parse_lessons(input('From: '), input('To: '))

else:
    print('You are already authorized.')

print(' -- Parse Tasks --')
if yl.get_status:
    yl.parse_tasks(input('From: '), input('To: '))

else:
    print('You are already authorized.')

yc = YandexContest()

yc.profile()

print(' -- Parse Contests --')
start = time.clock()
if yc.get_status:
    yc.parse(input('From: '), input('To: '), input('Word: '))

else:
    print('You are already authorized.')
    exit()
