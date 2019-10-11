#include <iostream>
#include<string>

struct ListNode {
      int val;           // define a value
      ListNode *next;    // define a pointer
      ListNode(int x) : val(x), next(NULL) {}   // constructor
 };



class Solution {
public:
    ListNode* removeElements(ListNode* head, int val) {
        
        ListNode *pseudo_head = new ListNode(0);
        pseudo_head->next = head;
        ListNode *cur = pseudo_head;

        while(cur){
            if (cur->next && cur->next->val == val){
                cur->next = cur->next->next;
            }
            else cur = cur->next;
        }
        return pseudo_head->next;

    }
};

