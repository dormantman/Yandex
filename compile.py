import time
import sys
from yandex import YandexLyceum, YandexContest

yl = YandexLyceum()

yl.load_cookies()
yl.profile()

print(' -- Parse Lessons --')
yl.parse_lessons(
    input('From: '), 
    input('To: ')
)

print(' -- Parse Tasks --')
yl.parse_tasks(
    input('From: '), 
    input('To: ')
)


yc = YandexContest()
yc.load_cookies()


start = time.clock()
yc.parse(
    input('From: '),
    input('To: '),
    input('Word: ')
)

while True:
    try:
        print('\b' * 100, end='')
        print('Time: %s' % (time.clock()-start), "\t Press Ctrl+D or Ctrl+C to exit.", end='')
        sys.stdout.flush()
        time.sleep(1)
    except KeyboardInterrupt:
        print("Exiting...")
        break
