#include <unordered_map>
using namespace std;

// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};

class Solution {
public:
    Node* copyRandomList(Node* head) {
        if (head == nullptr)
        {
            return nullptr;
        }
        unordered_map<Node*, Node*> old_to_new; // maps node in old list to its copy in the new list

        // Iterate through the old list, creating a copy of each node in the new list (if it hasn't already been created).
        Node* curr_node = head;
        Node* prev_node = nullptr;

        while (curr_node != nullptr)
        {
            Node* curr_node_copy;
            if (old_to_new.find(curr_node) != old_to_new.end())
            {
                curr_node_copy = old_to_new[curr_node];
            }
            else
            {
                curr_node_copy = new Node(curr_node->val);
            }

            // Assign curr_node->random (if necessary).
            if (curr_node->random != nullptr)
            {
                if (curr_node->random == curr_node)
                {
                    curr_node_copy->random = curr_node_copy;
                }
                else
                {
                    if (old_to_new.find(curr_node->random) != old_to_new.end())
                    {
                        curr_node_copy->random = old_to_new[curr_node->random];
                    }
                    else
                    {
                        // Create a copy of curr_node->random, and set curr_node_copy->random to it.
                        Node* curr_node_copy_random = new Node (curr_node->random->val);
                        curr_node_copy->random = curr_node_copy_random;
                        old_to_new[curr_node->random] = curr_node_copy_random;
                    }
                }
            }

            old_to_new[curr_node] = curr_node_copy;

            if (prev_node != nullptr)
            {
                old_to_new[prev_node]->next = curr_node_copy;
            }

            // Move to the next node in the original list.
            prev_node = curr_node;
            curr_node = curr_node->next;
        }

        return old_to_new[head];
    }
};