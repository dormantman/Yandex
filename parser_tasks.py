import json
import os
import threading

import bs4
import requests

if not os.access('yandex.py', os.F_OK):
    with open('yandex.py', 'wb') as file:
        file.write(requests.get('https://raw.githubusercontent.com/DormantMan/Yandex/master/yandex.py').content)

from yandex import YandexLyceum


class TasksParser(YandexLyceum):
    def __init__(self):
        super().__init__()
        self.tasks = {}
        self.info_tasks = [0, 0]  # ok, fail

    def _solve_task_(self, name, url):
        r = self.s.get(url)

        engine = bs4.BeautifulSoup(r.content, "lxml")
        body_a = engine.find_all('a')
        tasks = list(filter(lambda y: y and 'anytask.s3.yandex.net/files/' in y, map(lambda x: x.get('href'), body_a)))
        self.tasks[name]['solves'] = tasks

        nm = name
        while len(nm) < 50:
            nm += ' '

        st = self.tasks[name]['status']
        while len(st) < 15:
            st += ' '

        ss = self.tasks[name]['status'] == 'Зачтено'
        sim = 'OK' if ss else 'Fail'
        self.info_tasks[0] += 1 if ss else 0
        self.info_tasks[1] += 1 if not ss else 0

        print(nm, st, self.tasks[name]['score'], '\t', sim)

    def load_tasks(self):
        if not self.login:
            print('You are not authorized.')
            return False

        url = 'https://lms.yandexlyceum.ru/user/my_tasks'
        r = self.s.get(url)

        engine = bs4.BeautifulSoup(r.content, "lxml")
        body_a = engine.find_all('a')
        body_td = engine.find_all('td')

        tasks = list(filter(lambda y: y[1] is not None,
                            list(map(lambda x: (x.text.strip(), f"https://lms.yandexlyceum.ru{x.get('href')}" if x.get(
                                'href') and '/issue/' in x.get('href') else None), body_a))[14:]))
        txt = list(map(lambda x: x.text.strip(), body_td))

        self.tasks = {i[0]: {'url': i[1]} for i in tasks}

        for i in range(0, txt.__len__(), 6):
            if txt[i] not in self.tasks:
                self.tasks[txt[i]] = {'url': None}
            self.tasks[txt[i]]['date'] = txt[i + 3]
            self.tasks[txt[i]]['status'] = txt[i + 4]
            self.tasks[txt[i]]['score'] = txt[i + 5]

            if self.tasks[txt[i]]['url']:
                while threading.active_count() > 600:
                    pass
                threading.Thread(target=self._solve_task_, args=[txt[i], self.tasks[txt[i]]['url']]).start()

        while threading.active_count() > 1:
            pass

        print(f'Tasks Solve: {self.info_tasks[0]}\nTasks Fail: {self.info_tasks[1]}')

    def to_file(self, filename='dm.json'):
        """ Update file (non-viable) """

        # if os.access(filename, os.F_OK):
        #     with open(filename, 'r') as file:
        #         f = json.loads(file.read())
        #     self.tasks.update(f)
        with open(filename, 'w') as file:
            file.write(json.dumps(self.tasks))


if __name__ == '__main__':
    tp = TasksParser()
    tp.load_tasks()
    tp.to_file()
