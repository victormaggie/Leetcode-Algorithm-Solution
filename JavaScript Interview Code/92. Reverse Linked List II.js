var reverseBetween = function(head, m, n) {
    let dummy  = new ListNode(-1, head);
    let p = dummy;

    // first find the p value
    for (let i = 0; i < m-1; i++) p = p.next;
    // define the pointer here
    let b = p.next, c = b.next;
    for (let i = 0; i < n-m; i++) {
        const temp = c.next;
        c.next = b;
        b = c;
        c = temp;
    }
    p.next.next = c;
    p.next = b;
    return dummy.next;
}

// one pass solution.
