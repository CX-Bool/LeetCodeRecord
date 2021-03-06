/*
 * @lc app=leetcode.cn id=110 lang=cpp
 *
 * [110] 平衡二叉树
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
#include <algorithm>
using namespace std;
class Solution {
public:
    bool isBalanced(TreeNode* root) {
        if(!root) return true;
        return abs(height(root->left)-height(root->right))<=1 &&
                isBalanced(root->left) &&
                isBalanced(root->right);
                
    }
    int height(TreeNode* root){
        if(!root) return 0;
        else return max(height(root->left), height(root->right))+1;
    }
};
// @lc code=end

