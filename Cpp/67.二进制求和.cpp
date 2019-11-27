/*
 * @lc app=leetcode.cn id=67 lang=cpp
 *
 * [67] 二进制求和
 */

// @lc code=start
#include <string>
#include <iostream>
#include <algorithm>
using namespace std;
class Solution {
public:
    string addBinary(string a, string b) {
        string rres = "";
        int last = 0;
        int max_len = a.size() > b.size() ? a.size() : b.size();
        max_len += 1;
        string a_pre(max_len - a.size(), '0');
        string b_pre(max_len - b.size(), '0');
        a = a_pre + a;
        b = b_pre + b;
        for (int i = max_len - 1; i >= 0;i--){
            last += a[i] + b[i] - '0' - '0';
            if(last>1){
                rres += '0' + last - 2;
                last = 1;
            }
            else {
                rres += '0' + last;
                last = 0;
            }
        }
        if(*rres.rbegin() == '0'){
            rres.pop_back();
        }
        reverse(rres.begin(), rres.end());
        return rres;
    }
};
// @lc code=end

