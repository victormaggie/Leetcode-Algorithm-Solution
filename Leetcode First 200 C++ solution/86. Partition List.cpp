
// Given a linked list and a value x, partition it such that all nodes less than x come before nodes
// greater than or equal to x;


struct ListNode {
	
	int val;
	ListNode *next;
	ListNode() : val(0), next(nullptr) {}
	ListNode(int x) : val(x), next(nullptr) {}
	ListNode(int x, ListNode *next) : val(x), next(next) {}

};

class Solution {
public:
	ListNode* partition(ListNode* head, int x) {
		
		auto left = new ListNode(-1), right = new ListNode(-1);
		auto l = left, r = right;
		
		for (auto p = head; p ; p = p-> next) {
			if (p->val < x) l = l->next = p;
			else r = r->next = p;
		}
		l->next = r->next;
		r->next = NULL;
		
		return left->next;
	}
}
