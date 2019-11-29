/*
 * @lc app=leetcode.cn id=107 lang=cpp
 *
 * [107] 二叉树的层次遍历 II
 */

// @lc code=start

//Definition for a binary tree node.



#include <algorithm>
#include <vector>
#include <queue>
using namespace std;
// struct TreeNode {
//     int val;
//     TreeNode *left;
//     TreeNode *right;
//     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
// };
class Solution {
public:
    vector<vector<int>> levelOrderBottom(TreeNode* root) {
        vector<std::vector<int>> res;
        if(!root)
            return res;
        this->addNode(res, root, 0);
        return vector<std::vector<int>>(res.rbegin(), res.rend());
    }
private:
    void addNode(vector<vector<int>>& vec, TreeNode* node, int level){
        if(vec.size()<=level)
            vec.push_back(vector<int>());
        vec[level].push_back(node->val);
        if(node->left)
            this->addNode(vec, node->left, level+1);
        if(node->right)
            this->addNode(vec, node->right, level+1);
    }
};
// @lc code=end

