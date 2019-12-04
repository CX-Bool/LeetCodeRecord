/*
 * @lc app=leetcode.cn id=125 lang=cpp
 *
 * [125] 验证回文串
 */

// @lc code=start
#include <cctype>
#include <string>
using namespace std;
class Solution {
public:
    bool isPalindrome(string s) {
        int i=0,j=s.length()-1;
        while(i<=j){
            if(isalnum(s[i]) && isalnum(s[j])){
                if(tolower(s[i])!=tolower(s[j])) return false;
                i++;
                j--;
            }
            else if(!isalnum(s[i])) i++;
            else if(!isalnum(s[j])) j--;
        }
        return true;
    }
};
// @lc code=end

