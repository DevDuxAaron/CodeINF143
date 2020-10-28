from collections import deque


class PriorityQueue(object):
    def __init__(self):
        self.queue = []

    def __str__(self):
        return ' '.join([str(i) for i in self.queue])


    def isEmpty(self):
        return len(self.queue) == 0

    def insert(self, data):
        self.queue.append(data)

    def delete(self):
        try:
            max = 0
            for i in range(len(self.queue)):
                if self.queue[i] > self.queue[max]:
                    max = i
            item = self.queue[max]
            del self.queue[max]
            return item
        except IndexError:
            print()
            exit()

while True:
    try:
        pila = []
        cola = deque()
        colaPri = PriorityQueue()

        spam = True
        eggs = True
        foo = True

        nro = int(input())
        for i in range(nro):
            op, x = map(int, input().split())
            if op == 1:
                pila.append(x)
                cola.append(x)
                colaPri.insert(x)
            else:
                if spam:
                    if pila.pop() != x:
                        spam = False
                if eggs:
                    if cola.popleft() != x:
                        eggs = False
                if foo:
                    if colaPri.delete() != x:
                        foo = False

        c = [spam, eggs, foo].count(True)
        if c > 1:
            print("not sure")
        elif c == 0:
            print("impossible")
        else:
            if spam:
                print("stack")
            if eggs:
                print("queue")
            if foo:
                print("priority queue")

    except EOFError:
        break