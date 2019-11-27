/*
 * @lc app=leetcode.cn id=38 lang=cpp
 *
 * [38] 报数
 */

// @lc code=start
#include<string>
using namespace std;
class Solution {
public:
    string countAndSay(int n) {
        string s = "1";
        while(n-->1){
            s = this->forward(s);
        }
        return s;
    }
private:
    string forward(string s){
        string res = "";
        char pre = s[0];
        int count = 0;
        for (int i = 0; i < s.length();i++){
            if(s[i]==pre)
                count++;
            else {
                res += to_string(count) + pre;
                count = 1;
                pre = s[i];
            }
        }
        res += to_string(count) + pre;
        return res;
    }
};
// @lc code=end

