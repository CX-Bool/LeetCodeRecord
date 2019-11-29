/*
 * @lc app=leetcode.cn id=108 lang=cpp
 *
 * [108] 将有序数组转换为二叉搜索树
 */

// @lc code=start
/**
  Definition for a binary tree node.
  struct TreeNode {
      int val;
      TreeNode *left;
      TreeNode *right;
      TreeNode(int x) : val(x), left(NULL), right(NULL) {}
  };
 */
#include <vector>
#include <iostream>
using namespace std;

//   struct TreeNode {
//       int val;
//       TreeNode *left;
//       TreeNode *right;
//       TreeNode(int x) : val(x), left(NULL), right(NULL) {}
//   };
class Solution {
public:
    TreeNode* sortedArrayToBST(vector<int>& nums) {
        if(nums.size()==0)
            return NULL;
        int mid = nums.size()/2;
        TreeNode* root = new TreeNode(nums[mid]);
        vector<int> leftHalf, rightHalf;
        if(mid>=0)
            leftHalf = vector<int>(nums.begin(), nums.begin()+mid);
            root->left = this->sortedArrayToBST(leftHalf);
        if(nums.begin()+mid+1<=nums.end())
            rightHalf = vector<int>(nums.begin()+mid+1,nums.end());
            root->right = this->sortedArrayToBST(rightHalf);
        return root;
    }
};
// @lc code=end

