class Stack:
    def __init__(self):
        self.stack = list()

    def push(self, number):
        self.stack.append(number)

    def pop(self):
        if self.isEmpty():
            return False
        self.stack.pop()

    def isEmpty(self):
        return len(self.stack) == 0



