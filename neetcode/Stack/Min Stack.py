from collections import deque
class MinStack(object):

    def __init__(self):
        self.buffer=deque()
        

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.buffer.append(val)
        

    def pop(self):
        """
        :rtype: None
        """
        self.buffer.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.buffer[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return min(self.buffer)
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
