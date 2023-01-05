class Stack:
    def __init__(self):
        self.MAX_SIZE = 10
        self.stack = list()

    def push(self, number):
        if self.isFull():
            return False
        self.stack.append(number)

    def pop(self):
        if self.isEmpty():
            return False
        self.stack.pop()

    def isEmpty(self):
        return len(self.stack) == 0

    def isFull(self):
        return len(self.stack) + 1 == self.MAX_SIZE


a = Stack()

for i in range(10):
    a.push(i)

print(a.push(11))

for _ in range(10):
    a.pop()

print(a.pop())
