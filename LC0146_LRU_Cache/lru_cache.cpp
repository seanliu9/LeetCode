#include <unordered_map>
using namespace std;

class Node
{
public:
    int val;
    Node* prev = nullptr;
    Node* next = nullptr;

    Node(const int value) : val(value){}
};

class DoublyLinkedList
{
public:
    Node* head;
    Node* tail;

    DoublyLinkedList() : head(nullptr), tail(nullptr){}

    DoublyLinkedList(Node* h) : head(h), tail(h){}

    Node* remove(Node* n)
    {
        if (n == nullptr)
        {
            return nullptr;
        }
        if (n->prev != nullptr)
        {
            n->prev->next = n->next;
        }
        if (n->next != nullptr)
        {
            n->next->prev = n->prev;
        }
        if (this->head == n)
        {
            this->head = n->next;
        }
        if (this->tail == n)
        {
            this->tail = n->prev;
        }
        n->next = nullptr;
        n->prev = nullptr;
        return n;
    }
};

class LRUCache {
private:
    unordered_map<int, int>* cache = new unordered_map<int, int>();
    size_t curr_size = 0;
    size_t cap = 0;
    unordered_map<int, Node*>* nodes_map = new unordered_map<int, Node*>(); // maps cache key to the Node that represents it
    DoublyLinkedList* dll = new DoublyLinkedList(); // head = least recently used key, tail = most recently used key

public:
    LRUCache(int capacity) {
        this->cap = capacity;
    }

    void set_new_tail(const int key)
    {
        Node* mru; // represents the most recently used key
        if (this->nodes_map->find(key) != this->nodes_map->end())
        {
            // if key already exists in dll
            mru = this->dll->remove((*this->nodes_map)[key]);
        }
        else
        {
            // key doesn't exist in dll, so we create a new node corresponding to this key
            mru = new Node(key);
            (*this->nodes_map)[key] = mru;
        }
        // Set mru to be dll's new tail.
        if (this->dll->tail == nullptr)
        {
            this->dll->head = this->dll->tail = mru;
        }
        else
        {
            this->dll->tail->next = mru;
            mru->prev = this->dll->tail;
            this->dll->tail = mru;
        }
    }
    
    int get(int key) {
        if (this->cache->find(key) != this->cache->end())
        {
            // key becomes the most recently used, so make it the tail of dll
            this->set_new_tail(key);
            return (*this->cache)[key];
        }
        else
        {
            return -1;
        }
    }
    
    void put(int key, int value) {
        if (this->cache->find(key) != this->cache->end())
        {
            // If key already exists in cache, simply update its value.
            (*this->cache)[key] = value;
        }
        else 
        {
            if (this->curr_size < this->cap) 
            {
                this->curr_size++;
            } 
            else 
            {
                // Evict the last recently used key (i.e. dll's head).
                int target = this->dll->head->val;
                this->cache->erase(target);
                Node* evicted = this->dll->remove(this->dll->head);
                this->nodes_map->erase(target);
                delete evicted;
            }
            (*this->cache)[key] = value;
        }
        // key becomes the most recently used, so make it the tail of dll
        this->set_new_tail(key);
    }
};