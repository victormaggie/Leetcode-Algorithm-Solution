var removeNthFromEnd = function(head, n) {

    let cnt = 0, p = head;
    while (p) {
        p = p.next;
        cnt ++;
    }
    if (cnt == n) return head.next;

    p = head;
    let times = cnt - n - 1;

    while (times--) p = p.next;
    p.next = p.next.next;
    return head;
}


var removeNthFromEnd = function(head, n) {
    let fast = slow = dummyHead = new ListNode();
    fast.next = head;
    while(n--) fast = fast.next;
    while (fast.next) {
        fast = fast.next;
        slow = slow.next;
    }
    slow.next = slow.next.next;
    return dummyHead.next;
}

//o(n) one pass here!

