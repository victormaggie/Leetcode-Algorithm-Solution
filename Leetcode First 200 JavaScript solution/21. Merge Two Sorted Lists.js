var mergeTwoLists = function(l1, l2) {

    let dummy = new ListNode(1, l1);
    let p = dummy;

    while (l1 && l2) {
        if (l1.val <= l2.val) {
            p.next = l1;
            p = p.next;
            l1 = l1.next
        } else {
            p.next = l2;
            p = p.next;
            l2 = l2.next;
        }
    }

    if (l1) p.next = l1;
    if (l2) p.next = l2;
    return dummy.next;
};

// o(n+m)


