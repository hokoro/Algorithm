# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

class Solution(object):
    def __init__(self):
        self.stack = []
        self.transaction = 0
        self.trans = []
        self.bei = False
        self.com = False

    def push(self, value):
        if self.transaction > 0 and self.bei:
            self.trans.append([self.transaction, 'push', value])
            self.bei = False
        self.stack.append(value)

    def top(self):
        if len(self.stack) == 0:
            return 0
        if self.transaction > 0 and self.bei:
            self.trans.append([self.transaction, 'top'])
            self.bei = False

        return self.stack[-1]

    def pop(self):
        if len(self.stack) == 0:
            pass
        if self.transaction > 0 and self.bei:
            self.trans.append([self.transaction, 'pop', self.stack[-1]])
            self.bei = False
        return self.stack.pop()

    def begin(self):
        self.transaction += 1
        self.bei = True
        self.com = False
    def rollback(self):
        self.bei = False
        self.transaction -= 1
        if len(self.trans) == 0:
            return False
        if self.com:
            self.trans.pop()
            for i in range(len(self.trans),-1):
                if self.trans[i][1] == 'push':
                    self.stack.pop(self.stack.index(self.trans[i][2]))
                    self.trans.pop()
                    continue
                if self.trans[i][1] == 'pop':
                    self.stack.append(self.trans[i][1])
                    self.trans.pop()
                    continue
                if self.trans[i][1] == 'top':
                    continue
        if self.trans[-1][1] == 'push':
            self.stack.pop()
            self.trans.pop()
        if self.trans[-1][1] == 'pop':
            self.stack.append(self.trans[2])
            self.trans.pop()
        if self.trans[-1][1] == 'top':
            self.trans.pop()
            pass
        return True



        return True

    def commit(self):
        if not self.bei:
            return False
        self.bei = False
        self.com = True
        self.trans.append([self.transaction, 'commit'])
        for trans in self.trans:
            if trans[1] == 'push':
                self.stack.append(trans[2])
            if trans[1] == 'top':
                return self.stack[-1]
            if trans[1] == 'pop':
                return self.stack.pop()

        if len(self.trans) == 0:
            return False
        else:
            return True


def test():
    # Define your tests here
    sol = Solution()
    sol.push(4)
    sol.begin()
    sol.push(7)
    sol.begin()
    sol.push(2)
    sol.rollback()
    print(sol.top())
    sol.begin()
    sol.push(10)
    sol.commit()
    print(sol.top())
    print(sol.trans)
    print(sol.rollback())
    print(sol.top())
    print(sol.commit())


test()