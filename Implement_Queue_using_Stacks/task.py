class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def push(self, x):
        new_node = Node(x)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.head is None:
            return None
        value = self.head.value
        self.head = self.head.next
        return value

    def peek(self):
        if self.head is None:
            return None
        return self.head.value

    def empty(self):
        return self.head is None


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
