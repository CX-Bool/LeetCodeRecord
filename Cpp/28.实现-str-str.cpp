/*
 * @lc app=leetcode.cn id=28 lang=cpp
 *
 * [28] 实现 strStr()
 */

// @lc code=start
#include<string>
using namespace std;
class Solution {
public:
    int strStr(string haystack, string needle) {
        bool isfound;
        int maxi = haystack.length() - needle.length();
        if(maxi<0)
            return -1;
        for (int i = 0; i <= maxi;i++){
            isfound = true;
            for (int j = 0; j < needle.length();j++){
                if(haystack[i+j]!=needle[j]){
                    isfound = false;
                    break;
                }
            }
            if(isfound)
                return i;
        }
        return -1;  
    }
};
// @lc code=end

