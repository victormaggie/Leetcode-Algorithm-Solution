var getIntersectionNode = function(headA, headB) {

    if (!headA || !headB) return null;

    let A = headA, B = headB;

    while (headA != headB) {
        headA = headA ? headA.next : B;
        headB = headB ? headB.next : A;
    }

    return headA;
};

// Using the a + b + c = b + c + a solution --> it will meet at the intersection