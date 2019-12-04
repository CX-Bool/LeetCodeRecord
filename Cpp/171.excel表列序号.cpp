/*
 * @lc app=leetcode.cn id=171 lang=cpp
 *
 * [171] Excel表列序号
 */

// @lc code=start
#include<string>
using namespace std;
class Solution {
public:
    int titleToNumber(string s) {
        int res=0;
        for(int i=0;i<s.length();i++){
            res *= 26;
            res += s[i]-'A'+1;
        }
        return res;
    }
};
// @lc code=end

