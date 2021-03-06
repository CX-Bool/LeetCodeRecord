'''执行用时 :
60 ms
, 在所有 Python 提交中击败了
94.67%
的用户
内存消耗 :
15.6 MB
, 在所有 Python 提交中击败了
13.45%
的用户'''


class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minstack = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)
        if not self.minstack or self.minstack[-1] >= x:
            self.minstack.append(x)

    def pop(self):
        """
        :rtype: None
        """

        if self.minstack[-1] == self.stack[-1]:
            self.minstack.pop()
        self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.minstack[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()