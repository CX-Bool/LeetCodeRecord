/*
 * @lc app=leetcode.cn id=111 lang=cpp
 *
 * [111] 二叉树的最小深度
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
class Solution {
public:
    int minDepth(TreeNode* root) {
        if(!root) return 0;
        else if(!root->left && !root->right) return 1;
        else if(!root->left) return minDepth(root->right)+1;
        else if(!root->right) return minDepth(root->left)+1;
        return std::min(minDepth(root->left), minDepth(root->right))+1;
    }
};
// @lc code=end

