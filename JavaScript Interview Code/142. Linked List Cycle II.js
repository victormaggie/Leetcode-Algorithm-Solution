


var detectCycle = function(head) {
    let fast = head;
    let slow = head;

    // here we need to make sure the fast and fast.next value
    while (fast.next != null && fast.next.next != null) {
        fast = fast.next.next;
        slow = slow.next;
        if (fast == slow) {
            slow = head;
            // find the starting point;
            while (fast != slow) {
                fast = fast.next;
                slow = slow.next;
            }
            return slow;
        }
    }
    return null;
}