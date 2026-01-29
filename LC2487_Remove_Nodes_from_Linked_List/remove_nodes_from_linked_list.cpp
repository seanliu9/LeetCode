struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

#include <iostream>
using namespace std;

class Solution {
public:
    ListNode* rRemoveNodes(ListNode* curr)
    {
        if (curr->next == nullptr)
        {
            // base case
            return curr;
        }
        curr->next = this->rRemoveNodes(curr->next);
        if (curr->val < curr->next->val)
        {
            // if we need to remove curr
            return curr->next;
        }
        else
        {
            // no need to remove curr
            return curr;
        }
    }

    ListNode* removeNodes(ListNode* head) {
        return this->rRemoveNodes(head);
    }
};