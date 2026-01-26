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
private:
    int max_right;

public:
    Solution()
    {
        this->max_right = 0;
    }

    ListNode* rRemoveNodes(ListNode* curr, ListNode* prev)
    {
        if (curr->next == nullptr)
        {
            // base case
            this->max_right = curr->val;
            return curr;
        }
        else
        {
            this->rRemoveNodes(curr->next, curr);
            if (curr->val < this->max_right)
            {
                // Remove curr.
                if (prev == nullptr)
                {
                    // if we need to remove curr but it's the first node in the list
                    ListNode* result = curr->next;
                    delete curr;
                    return result;
                }
                else
                {
                    prev->next = curr->next;
                    delete curr;
                    return prev->next;
                }
            }
            else
            {
                // no need to remove curr
                this->max_right = curr->val;
                return curr;
            }
        }
    }

    ListNode* removeNodes(ListNode* head) {
        return this->rRemoveNodes(head, nullptr);
    }
};

int main()
{
    // ListNode* head = new ListNode(5);
    // head->next = new ListNode(2);
    // head->next->next = new ListNode(13);
    // head->next->next->next = new ListNode(3);
    // head->next->next->next->next = new ListNode(8);

    
    ListNode* head = new ListNode(3);
    head->next = new ListNode(4);
    head->next = new ListNode(6);
    head->next = new ListNode(150);

    Solution sol;
    ListNode* answer = sol.removeNodes(head);
    std::cout << "final list's head = " << answer->val;
}