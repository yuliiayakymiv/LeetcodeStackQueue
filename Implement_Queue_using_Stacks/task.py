class Stack:
    def __init__(self):
        self.items = []

    def push(self, x):
        self.items.append(x)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def empty(self):
        return len(self.items) == 0


class MyQueue:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def push(self, x):
        self.stack1.push(x)

    def pop(self):
        while not self.stack1.empty():
            self.stack2.push(self.stack1.pop())
        result = self.stack2.pop()

        while not self.stack2.empty():
            self.stack1.push(self.stack2.pop())

        return result

    def peek(self):
        while not self.stack1.empty():
            self.stack2.push(self.stack1.pop())
        result = self.stack2.peek()

        while not self.stack2.empty():
            self.stack1.push(self.stack2.pop())

        return result

    def empty(self):
        return self.stack1.empty()


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
