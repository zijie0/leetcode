class MinStack:
    # @param x, an integer
    # @return an integer
    def __init__(self):
        self.stack = []
        self.min_stack = []
        self.idx = 0
    def push(self, x):
        if not self.min_stack:
            self.min_stack.append(self.idx)
        elif x < self.stack[self.min_stack[-1]]:
            self.min_stack.append(self.idx)
        self.stack.append(x)
        self.idx += 1

    # @return nothing
    def pop(self):
        if self.idx-1 == self.min_stack[-1]:
            self.min_stack.pop()
        self.stack.pop()
        self.idx -= 1

    # @return an integer
    def top(self):
        return self.stack[-1]

    # @return an integer
    def getMin(self):
        return self.stack[self.min_stack[-1]]

t = MinStack()
t.push(2)
t.push(0)
t.push(3)
t.push(0)
print t.getMin()
t.pop()
print t.getMin()
t.pop()
print t.getMin()
t.pop()
print t.getMin()