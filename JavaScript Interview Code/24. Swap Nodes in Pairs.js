
var swapPairs = function(head) {
    let dummy = new ListNode(0);
    dummy.next = head;
    slow = dummy;

    while (head && head.next) {
        let first_node = head;
        let second_node = head.next;

        slow.next = second_node;
        first_node.next = second_node.next;
        second_node.next = first_node;

        //swap head node
        slow = first_node;
        head = first_node.next;
    }
    return dummy.next;
}

// time complexity o(n)


// We can only use one node here
// this code is neat !!

var swapPairs = function(head) {
    let dummy = new ListNode(0);
    dummy.next = head;
    curr = dummy;

    while (curr.next && curr.next.next) {
        let first_node = curr.next;
        let second_node = curr.next.next;

        // swap here
        curr.next = second_node;
        second_node.next = first_node;
        first_node.next = second_node.next;

        // move curr node
        curr = first_node;
    }
    return dummy.next;
}


// we can also use the recursion method

var swapPairs = function(head) {
    if ((!head) || (!head.next)) return head;

    // first node and second node
    let first_node = head;
    let second_node = head.next;

    // swapping here
    first_node.next = swapPairs(second_node.next);
    second_node.next = first_node;

    return second_node;
}

// time complexity o(n)
// space complexity o(n)
