from yandex import YandexLyceum, YandexContest
import time
import sys
yl = YandexLyceum()
yl.load_cookies()


yl.profile()

print(' -- Parse Lessons --')
yl.parse_lessons(input('From: '), input('To: '))

print(' -- Parse Tasks --')
yl.parse_tasks(input('From: '), input('To: '))
#yl.parse_tasks(10400, 10500)


yc = YandexContest()
yc.load_cookies()


start = time.clock()
yc.parse(input('From: '), input('To: '))

while True:
    try:
        print('\b' * 100, end='')
        print('Time: %s' % (time.clock()-start), "\t Press Ctrl+D or Ctrl+C to exit.", end='')
        sys.stdout.flush()
        time.sleep(1)
    except KeyboardInterrupt:
        print("Exiting...")
        break
