//
// Created by Jiang,Xinyang on 2020/7/27.
//

#include <iostream>
#include <vector>

using namespace std;


struct ListNode {
    int val;
    struct ListNode *next;

    ListNode(int x) :
            val(x), next(NULL) {
    }
};


vector<int> printListFromTailToHead(ListNode* head) {
    vector<int> result;
    if (head == nullptr)
        return result;

    ListNode* cur = head;
    while(cur != nullptr){
        result.insert(result.begin(), cur->val);
        cur = cur->next;
    }

    return result;
}


int main() {

    ListNode* a = new ListNode(1);
    ListNode* b = new ListNode(2);
    ListNode* c = new ListNode(3);
    a->next = b;
    b->next = c;

    vector<int> res = printListFromTailToHead(a);

    for (int x : res)
        cout << x << " ";
    cout << endl;

    delete a;
    delete b;
    delete c;
}