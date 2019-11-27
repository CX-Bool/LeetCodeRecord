/*
 * @lc app=leetcode.cn id=58 lang=cpp
 *
 * [58] 最后一个单词的长度
 */

// @lc code=start
#include <string>
using namespace std;
class Solution {
public:
    int lengthOfLastWord(string s) {
        bool isfind = false;
        int count=0;
        for (int i = s.length() - 1; i >= 0;i--){
            if(s[i]!=' '){
                isfind = true;
                count += 1;
            }
            else if (isfind) {
                return count;
            }
        }
        return count;
    }
};
// @lc code=end

