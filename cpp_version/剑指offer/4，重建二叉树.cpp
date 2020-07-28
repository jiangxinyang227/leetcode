//
// Created by Jiang,Xinyang on 2020/7/27.
//

#include <iostream>
#include <vector>
#include <queue>

using namespace std;


struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;

    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};


TreeNode *rebuild(vector<int> &pre, int pre_left, int pre_right, vector<int> &vin, int vin_left, int vin_right) {
    if (pre_left > pre_right)
        return nullptr;
    TreeNode *node = new TreeNode(pre[pre_left]);
    for (int i = vin_left; i < vin_right; i++) {
        if (pre[pre_left] == vin[i]) {
            node->left = rebuild(pre, pre_left + 1, pre_left + i - vin_left, vin, vin_left, i - 1);
            node->right = rebuild(pre, pre_left + i - vin_left + 1, pre_right, vin, i + 1, vin_right);
        }
    }
    return node;
}

TreeNode *reConstructBinaryTree(vector<int> pre, vector<int> vin) {
    if (pre.empty() && vin.empty())
        return nullptr;
    if (pre.size() != vin.size())
        return nullptr;

    TreeNode *res = rebuild(pre, 0, pre.size() - 1, vin, 0, vin.size() - 1);
    return res;
}


void trackTree(TreeNode* tree){
    if (tree == nullptr)
        return;
    queue<TreeNode*> queue({tree});
    while(!queue.empty()){
        TreeNode* node = queue.front();
        cout << node->val << endl;
        queue.pop();
        if(node->left != nullptr)
            queue.push(node->left);
        if(node->right != nullptr)
            queue.push(node->right);
    }
}

int main() {

    vector<int> pre = {1, 2, 4, 5, 3, 6, 7};
    vector<int> vin = {4, 2, 5, 1, 6, 3, 7};

    TreeNode* res = reConstructBinaryTree(pre, vin);

    trackTree(res);
}