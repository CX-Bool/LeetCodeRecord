/*
 * @lc app=leetcode.cn id=13 lang=cpp
 *
 * [13] 罗马数字转整数
 */

// @lc code=start
#include<iostream>
#include<unordered_map>
#include<string>
using namespace std;
class Solution {
public:
    int romanToInt(string s) {
        unordered_map<char, int> dict;
        dict['I']=1;
        dict['V']=5;
        dict['X']=10;
        dict['L']=50;
        dict['C']=100;
        dict['D']=500;
        dict['M']=1000;
        int res =0, pre = 10086;
        int cur;
        for (int i = 0; i < s.size();i++){
            cur = dict[s[i]];
            res += cur;
            if(cur>pre)
                res -= 2 * pre;
            pre = cur;
        }
        return res;
    }
};
// @lc code=end

