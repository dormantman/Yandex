import time
import sys
from yandex import YandexLyceum, YandexContest

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

print(' -- Parse Contests --')
start = time.clock()
if yc.get_status:
    yc.parse(input('From: '), input('To: '), input('Word: '))
else:
    print('You are already authorized.')
    exit()

while True:
    try:
        print('\b' * 100, end='')
        print('Time: %s' % (time.clock()-start), "\t Press Ctrl+D or Ctrl+C to exit.", end='')
        sys.stdout.flush()
        time.sleep(1)
    except KeyboardInterrupt:
        print("Exiting...")
        break
