import queue
import time
from queue import Queue
from random import randint
from threading import Thread


class Table:
    # number = None

    def __init__(self, number, guest=None):
        self.number = number
        self.guest = guest


class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        paus = randint(3, 10)
        time.sleep(paus)


class Cafe:
    queue = Queue()

    def __init__(self, *args):
        self.tables = args

    def guest_arrival(self, *guests):
        self.thr = []
        le = len(guests)
        for i in range(le):
            for table in self.tables:
                if table.guest is None:
                    table.guest = guests[i]
                    print(f'{table.guest.name} сел(-а) за стол номер {table.number}')
                    guests[i].start()
                    self.thr.append(guests[i])
                    i += 1
                else:
                    i += 1
                    pass
            if i < le:
                self.queue.put(guests[i])
                print(f'{guests[i].name} в очереди')

    def discuss_guests(self):
        for t in self.thr:
            for table in self.tables:
                if table.guest == t:
                    t.join()
                    print(f'{t.name} покушал(-а) и ушёл(ушла)')
                    print(f'Стол номер {table.number} свободен')
                    table.guest = None
                    if not self.queue.empty():
                        t = self.queue.get()
                        table.guest = t
                        print(f'{t.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
                        t.start()
                        self.thr.append(t)
                    else:
                        continue


# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = ['Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
                'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra']
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()