class Queue:
    def __init__(self, n):
        self.MAX_SIZE = n
        self.queue = [None for _ in range(n)]
        self.front = 0
        self.rear = 0

    def Enqueue(self, data):
        if self.isFull():
            return False
        self.queue.append(data)
        self.rear += 1

    def Dequeue(self):
        if self.isEmpty():
            return False
        return self.queue.pop(0)

    def front(self):
        return self.queue[0]

    def rear(self):
        return self.queue[self.size()]

    def size(self):
        return self.rear - self.front

    def isEmpty(self):
        return len(self.queue) == 0

    def isFull(self):
        return (self.rear + 1) % self.MAX_SIZE == self.front


a = Queue(10)

for i in range(10):
    a.Enqueue(i)

print(a.Enqueue(11))

for _ in range(10):
    a.Dequeue()

print(a.Dequeue())
