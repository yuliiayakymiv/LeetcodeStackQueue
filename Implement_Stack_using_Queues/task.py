class QueueNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.first = None
        self.last = None

    def push(self, x):
        new_node = QueueNode(x)
        if self.empty():
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node

    def pop(self):
        if self.empty():
            return None
        value = self.first.value
        self.first = self.first.next
        if self.first is None:
            self.last = None
        return value

    def peek(self):
        if self.empty():
            return None
        return self.first.value

    def empty(self):
        return self.first is None


class MyStack:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self, x):
        self.q2.push(x)

        while not self.q1.empty():
            self.q2.push(self.q1.pop())

        self.q1, self.q2 = self.q2, self.q1

    def pop(self):
        return self.q1.pop()

    def top(self):
        return self.q1.peek()

    def empty(self):
        return self.q1.empty()
