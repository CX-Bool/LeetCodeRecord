/*
 * @lc app=leetcode.cn id=172 lang=cpp
 *
 * [172] 阶乘后的零
 */

// @lc code=start
class Solution {
public:
    int trailingZeroes(int n) {
        // int res=0,t;
        // for(int i=1;i<=n;i++){
        //     t=i;
        //     while(t%5==0){
        //         res+=1;
        //         t/=5;
        //     }
        // }
        // return res;
        int res=0,i=5;
        while(i<=n/5){
            res+= n/i;
            i*=5;
        }
        res+= n/i;
        return res;
    }
};
// @lc code=end

