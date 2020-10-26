var mergeKLists = function(lists) {
    
    let dummy = new ListNode(0);
    let node = dummy;
    let n = lists.length;
    
    while (true) {
        let p = -1;
        for (let i in lists) {
            if (lists[i]) p = i;
        }
        if (p == -1) break;
        // find the smallest value here
        for (let i = 0; i < n; i++) {
            if (lists[i] && lists[i].val < lists[p].val) {
                p = i;
            }
        }
        // get the node here
        node.next = new ListNode(lists[p].val);
        node = node.next;
        lists[p] = lists[p].next;
    }
    return dummy.next;
};


// o(n * k) --> solution 

// if using heap solution:   n log K   --> every time pop small, construct tree log K