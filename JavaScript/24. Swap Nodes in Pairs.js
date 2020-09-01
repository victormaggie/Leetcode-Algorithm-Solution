
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
