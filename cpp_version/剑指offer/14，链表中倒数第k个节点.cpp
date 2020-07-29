//
// Created by jiangxinyang on 2020-7-29.
//

#include <iostream>

using namespace std;


struct ListNode {
    int val;
    struct ListNode *next;
    ListNode(int x) :
            val(x), next(NULL) {
    }
};

class Solution {
public:
    ListNode* FindKthToTail(ListNode* pListHead, unsigned int k) {
        if (pListHead == nullptr || k <= 0)
            return nullptr;

        ListNode* pre = pListHead;
        for (int i = 0; i < k; i++){
            if (pre == nullptr)
                return nullptr;
            pre = pre->next;
        }

        ListNode* cur = pListHead;
        while (pre != nullptr){
            cur = cur->next;
            pre = pre->next;
        }
        return cur;
    }
};


int main() {

    Solution s;
    ListNode a(1);
    ListNode b(2);
    ListNode c(3);
    ListNode d(4);

    a.next = &b;
    b.next = &c;
    c.next = &d;

    ListNode* res = s.FindKthToTail(&a, 5);
    cout << res->val << endl;

}
