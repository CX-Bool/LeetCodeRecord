# 执行用时 : 64 ms, 在1-bit and 2-bit Characters的Python3提交中击败了13.44% 的用户
# 内存消耗 : 13.2 MB, 在1-bit and 2-bit Characters的Python3提交中击败了7.79% 的用户
class Solution:
    def isOneBitCharacter(self, bits: list[int]) -> bool:
        n = len(bits)
        i = 0
        while i < n:
            if i == n-1:
                return True
            elif i == n-2:
                if bits[i]:
                    return False
                else:
                    return True
            if bits[i] == 0:
                i += 1
            else:
                i += 2