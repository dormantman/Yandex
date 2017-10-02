from yandex import YandexLyceum, YandexContest
import time

yl = YandexLyceum()
yl.load_cookies()

if not yl.get_status():
    print('Username: ', end='')
    username = input()

    print('Password: ', end='')
    password = input()

    if yl.auth(username, password):
        yl.save_cookies()



yl.profile()

print(' -- Parse Lessons --')
yl.parse_lessons(input('From: '), input('To: '))

print(' -- Parse Tasks --')
yl.parse_tasks(input('From: '), input('To: '))
#yl.parse_tasks(10400, 10500)



yc = YandexContest()
yc.load_cookies()


if not yc.get_status():
    print('Username: ', end='')
    username = input()

    print('Password: ', end='')
    password = input()

    if yc.auth(username, password):
        yc.save_cookies()


start = time.clock()

yc.parse(input('From: '), input('To: '))

print('Time: %s' % (time.clock()-start))


input('Press Enter to Exit...')