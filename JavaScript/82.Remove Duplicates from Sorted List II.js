/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */

var deleteDuplicates = function(head) {

    if (!head) return null;

    // declare the variable
    let dummy = new ListNode(0);
    dummy.next = head;
    let slow = dummy;

    while (head && head.next) {
        if (head.val === head.next.val) {
            while (head.next && head.val === head.next.val) {
                head = head.next;
            }
            head = head.next;
            slow.next = head;
        } else {
            slow = slow.next;
            head = head.next;
        }
    }
    return dummy.next;
};

// o(n) time complexity