# 执行用时 : 80 ms, 在Available Captures for Rook的Python3提交中击败了100.00% 的用户
# 内存消耗 : 13.2 MB, 在Available Captures for Rook的Python3提交中击败了100.00% 的用户

# 在一个 8 x 8 的棋盘上，有一个白色车（rook）。也可能有空方块，白色的象（bishop）和黑色的卒（pawn）。它们分别以字符 “R”，“.”，“B” 和 “p” 给出。大写字符表示白棋，小写字符表示黑棋。
#
# 车按国际象棋中的规则移动：它选择四个基本方向中的一个（北，东，西和南），然后朝那个方向移动，直到它选择停止、到达棋盘的边缘或移动到同一方格来捕获该方格上颜色相反的卒。另外，车不能与其他友方（白色）象进入同一个方格。
#
# 返回车能够在一次移动中捕获到的卒的数量。


class Solution:
    def numRookCaptures(self, board: list[list[str]]) -> int:
        length = range(8)
        rook = None
        for r in length:
            for c in length:
                if board[r][c] == 'R':
                    rook = (r,c)
        res = 0
        for delta in [(0,-1),(-1,0),(0,1),(1,0)]:
            r,c = rook[0]+delta[0], rook[1]+delta[1]
            while 0<=r<8 and 0<=c<8:
                if board[r][c]=='B':
                    break
                if board[r][c]=='p':
                    res += 1
                    break
                r += delta[0]
                c += delta[1]
        return res

if __name__ == '__main__':
    Solution().numRookCaptures([['s']])
