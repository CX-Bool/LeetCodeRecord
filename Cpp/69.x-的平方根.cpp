/*
 * @lc app=leetcode.cn id=69 lang=cpp
 *
 * [69] x 的平方根
 */

// @lc code=start
#include <cmath>
class Solution {
public:
    int mySqrt(int x) {
        double f = std::sqrt(x);
        return std::floor(f);
    }
};
// @lc code=end

