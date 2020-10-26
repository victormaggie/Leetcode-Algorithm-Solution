var swapPairs = function(head) {

    // be sure that if chang the head node, we need use the dummy node
    // use the first and second pointer for this question.

    let dummy = new ListNode(1, head);
    let node  = dummy;

    while (node.next && node.next.next) {
        // define first and second node
        const firstNode = node.next;
        const secondNode = node.next.next;

        // swap here
        node.next = secondNode;
        firstNode.next = secondNode.next;
        secondNode.next = firstNode;

        // change the node
        node = node.next.next;
        // node = firstNode;
    }

    return dummy.next;

};