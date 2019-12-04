/*
 * @lc app=leetcode.cn id=168 lang=cpp
 *
 * [168] Excel表列名称
 */

// @lc code=start
#include <string>
using namespace std;
class Solution {
public:
    string convertToTitle(int n) {
        string res = "";
        char temp;
        int remainder=0;
        while(n){
            remainder=n%26;
            if(remainder==0){
                temp = 'Z';
                n=n/26-1;
            }
            else{
                temp='A'-1+remainder;
                n/=26;
            }
            res = temp + res;
        }
        return res;
    }
};
// @lc code=end

