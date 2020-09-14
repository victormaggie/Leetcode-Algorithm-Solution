var addTwoNumbers = function(l1, l2) {

    let memo = 0;
    const head = new ListNode(0);
    let ptr = head;
    let isExceed = 0;

    while (l1 || l2) {
        l1Val = l1 ? l1.val : 0;
        l2Val = l2 ? l2.val : 0;
        const sum = l1Val + l2Val + isExceed;

        isExceed = sum >= 10 ? 1 : 0;
        ptr.val = sum % 10;
        l1 = l1 ? l1.next : l1;
        l2 = l2 ? l2.next : l2;
        if (!l1 && !l2 && isExceed === 0) break;
        ptr.next = new ListNode(1);
        ptr = ptr.next;
    }
    return head;
};


// time complexity o(m)
// space complexity o(m)

// iterate solution here

var addTwoNumbers = function(l1, l2) {
    const result = new ListNode();
    let head = result;

    function traversal(n1, n2, sum, carry) {
        if (!n1 && !n2 && !carry) {
            return head.next;
        }
        let val = (n1 && n1.val) + (n2 && n2.val) + carry;
        carry = val > 9;
        sum.next = new ListNode(val % 10);
        return traversal((n1 && n1.next), (n2 && n2.next), sum.next, carry);
    }
    return traversal(l1, l2, result, 0);
}

// time complexity o(n)
// space complexity o(n)

