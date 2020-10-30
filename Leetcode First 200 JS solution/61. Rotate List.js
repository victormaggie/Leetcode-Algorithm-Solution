var rotateRight = function(head, k) {
    
    if (!head) return head;
    
    let cnt = 0;
    let tail;
    for (let p = head; p != null; p = p.next){
        
        tail = p;
        cnt ++;
    }
    
    k %= cnt;
    if (!k) return head;
    let p = head;    
    
    for (let i = 0; i < cnt - k - 1; i++) {
        p = p.next;
    }
    
    tail.next = head;
    head = p.next;
    p.next = null;
    return head;
    
};

// o (n)