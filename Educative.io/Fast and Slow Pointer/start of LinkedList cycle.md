# Find the start of the LinkedList cycle

 x = z


```
var detectCycle = function(head) {
    
    if (!head) return head;
    
    let fast = head, slow = head;
    while (fast.next && fast.next.next) {
        fast = fast.next.next;
        slow = slow.next
        if (fast == slow) {
            fast = head;
            while (fast != slow) {
                fast = fast.next;
                slow = slow.next;
            }
            return fast;
        }
    }
    return null;
};
```