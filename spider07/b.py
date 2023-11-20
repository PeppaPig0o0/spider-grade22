# import collections
#
# point = collections.namedtuple('Points', 'x y', defaults=(9,9))
# p1 = point(2, 3)
# p2 = point(4, 2)
# p3 = point()
#
# print(p1) # Points(x=2, y=3)
# print(p2) # Points(x=4, y=2)
# print(p3) # Points(x=4, y=2)
# for i in p1:
#     print(i)
import queue
q = queue.Queue()
q.put(7)
print(q.queue)


class Queue:
    def __init__(self, maxsize=None, lifo=False):
        self.__first = None
        self.__last = None
        self.maxsize = None
        self.queue = []
        self.lifo = lifo

    def push(self, item):
        if not self.lifo:
            self.queue.append(item)
        else:
            self.queue.insert(item, 0)

    def pop(self):
        if not self.lifo:
            self.__first = self.queue[0]
            del self.queue[0]
            return self.__first
        else:
            self.__last = self.queue[-1]
            del self.queue[-1]
            return self.__last

    def __push_one(self, item):
        if not self.lifo:
            self.queue.append(item)
        else:
            self.queue.insert(item, 0)

    def __get_one(self):
        if not self.lifo:
            self.queue.append(item)
        else:
            self.queue.insert(item, 0)

    def __del__(self):
        del self.queue
        del self.lifo