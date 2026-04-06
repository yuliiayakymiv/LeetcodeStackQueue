from collections import deque

class FreqStack:
    def __init__(self):
        self.freq = {}
        self.groups = {}
        self.max_freq = 0

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if val in self.freq:
            self.freq[val] = self.freq[val] + 1
        else:
            self.freq[val] = 1

        f = self.freq[val]

        if f > self.max_freq:
            self.max_freq = f

        if f not in self.groups:
            self.groups[f] = deque()
        self.groups[f].append(val)

    def pop(self):
        """
        :rtype: int
        """
        val = self.groups[self.max_freq].pop()

        if val in self.freq:
            self.freq[val] = self.freq[val] - 1

        if len(self.groups[self.max_freq]) == 0:
            self.max_freq = self.max_freq - 1

        return val

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
