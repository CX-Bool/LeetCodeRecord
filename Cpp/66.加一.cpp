/*
 * @lc app=leetcode.cn id=66 lang=cpp
 *
 * [66] 加一
 */

// @lc code=start
#include <vector>
using namespace std;
class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        int cur_val = 0;
        int last_val = 1;
        vector<int>::reverse_iterator riter = digits.rbegin();
        for(;riter!=digits.rend();riter++){
            cur_val = *riter;
            cur_val += last_val;
            if(cur_val>9){
                cur_val -= 10;
                last_val = 1;
            }
            else {
                last_val = 0;
            }
            *riter = cur_val;
        }
        if(last_val==1){
            digits.insert(digits.begin(), 1);
        }
        return digits;
    }
};
// @lc code=end

