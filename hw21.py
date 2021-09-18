# Написать функцию-генератор, которая объединяет два отсортированных итератора.
# Результирующий итератор должен содержать последовательность в которой содержаться все элементы из каждой коллекции, в упорядоченном виде.

# list(merge((x for x in range(1,4)),(x for x in range(2,5)))) == [1,2,2,3,3,4]



class MyIter(object):

    def __init__(self, iterator):
        self.iterator = iterator
        self.next_val = None
        self.finished = False
        self.__next__()

    def __next__(self):  
        if self.finished:
            return
        value = self.next_val
        try:
            self.next_val = next(self.iterator)
        except StopIteration:
            self.finished = True
        return value


def merge(iter1, iter2):

    wrap1, wrap2 = MyIter(iter1), MyIter(iter2)

    while not (wrap1.finished and wrap2.finished):
        if (wrap2.finished or
               (not wrap1.finished and
                wrap1.next_val <= wrap2.next_val)):
            yield wrap1.__next__()
        else:
            yield wrap2.__next__()

for item in merge((x for x in range(1, 4)), (x for x in range(2, 5))):
        print(item, end=' ')