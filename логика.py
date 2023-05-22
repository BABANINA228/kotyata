# -*- coding: UTF-8 -*-
import time
import json

class Prioritet:
    count = 0
    list = []
    def __init__(self, name, priority, urgency):
        self.name = name
        self.priority = priority
        self.urgency = urgency
        Prioritet.count += 1
        self.list.append(self)
    def __str__(self):
        return f"{self.name, self.priority, self.urgency}"

def new(name, priority, urgency):
    a = Prioritet(name, priority, urgency)

dict = {}

new("Niger", 2, '2апвапавпв')
new("Work", 1, 7)

Prioritet.list = sorted(Prioritet.list, key=lambda x: x.priority)

for i in range(Prioritet.count):
    dict[f'{Prioritet.list[i].name}']=f'{Prioritet.list[i].priority}', f'{Prioritet.list[i].urgency}'

    # dict.fromkeys(Prioritet.list[i].priority[Prioritet.list[i].priority])
    # print(Prioritet.list[i].priority)



with open("tasks.json", "w") as file:
	json.dump(dict, file, indent = 4, ensure_ascii=False)

import codecs
with codecs.open("tasks.json", "r") as file:
	 a = file.read()
print(a)
print('Маму ебал')


# t = []
# time1 = time.localtime(time.time())
# print(time.localtime(time.time()))
# # for i in range(0,8):
# #     t.append(time1[i])
# # print(t)
# time2 = time.mktime(time1)
# print(time2)
# print(prioritet.__dict__)


# Перетаскивание задачи
# Определение прогой приоритетов
