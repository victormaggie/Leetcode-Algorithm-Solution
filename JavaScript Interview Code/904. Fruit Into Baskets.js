var totalFruit = function(tree) {

    let windowStart = 0;
    let dict = {};
    let maxLength = 0;
    for (let windowEnd = 0; windowEnd < tree.length; windowEnd++) {
        currentFruit = tree[windowEnd];
        if (!(currentFruit in dict)) {
            dict[currentFruit] = 0;
        }
        dict[currentFruit] += 1;
        while (Object.keys(dict).length > 2) {
            leftFruit = tree[windowStart];
            dict[leftFruit] -= 1;
            if (dict[leftFruit] === 0) delete dict[leftFruit];
            windowStart += 1;
        }
        maxLength = Math.max(maxLength, windowEnd - windowStart + 1);
    }
    return maxLength;
};

// time complexity o(n)
// space complexity o(n)


var totalFruit = function(tree) {
    let windowStart = 0;
    let dict = {};
    let maxLength = 0;

    for (let windowEnd = 0; windowEnd < tree.length; windowEnd++) {
        currentFruit = tree[windowEnd];
        dict[currentFruit] = (dict[currentFruit || 0]) + 1;
        while (Object.keys(dict) > 2) {
            leftFruit = tree[windowStart];
            dict[leftFruit] -= 1;
            if (dict[leftFruit] === 0) delete dict[leftFruit];
            leftFruit++;
        }
        maxLength = Math.max(maxLength, windowEnd - windowStart + 1);
    }
    return maxLength;
}

