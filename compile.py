from yandex import YandexLyceum, YandexContest
import time

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
print('Time: %s' % (time.clock()-start))


input('Press Enter to Exit...')
