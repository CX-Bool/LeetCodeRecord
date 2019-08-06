class Solution:
    def decodeString(self, s: str) -> str:
        res=''
        stack=[]
        for c in s:
            if c != ']':
                stack.append(c)
            else:
                temps=''
                top = stack.pop()
                while top != '[':
                    #temps.insert(0,top)
                    temps = top + temps
                    top = stack.pop()
                    print(stack)
                tempnum=''
                while stack and stack[-1] and stack[-1].isdigit():
                    #tempnum.insert(0,stack.pop())
                    top = stack.pop()
                    tempnum=top+tempnum
                if tempnum:
                    temps = int(tempnum)*temps
                if stack:
                    stack.append(temps)
                else:
                    res += temps
        return res+''.join(stack)

if __name__ == '__main__':
    s = '3[a]2[bc]'
    print(Solution().decodeString(s))