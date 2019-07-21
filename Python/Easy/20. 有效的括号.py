class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        match = {')': '(', '}': '{', ']': '['}
        stack = []
        for c in s:
            if c in '([{':
                stack.append(c)
            else:
                if stack and stack[-1] == match[c]:
                    stack.pop()
                else:
                    return False
        else:
            return not stack
