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



# a = Prioritet(1, 1, 2)
new("Домашнее задание", 2, 2)
new("Работа", 1, 7)

Prioritet.list = sorted(Prioritet.list, key=lambda x: x.priority)
print(Prioritet.list)
for i in range(Prioritet.count):
    print(Prioritet.list[i])

with open("tasks.json", "w") as file:
	json.dump(Prioritet.list, file, indent = 4, ensure_ascii=False)



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
