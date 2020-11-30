var isValid = function(s) {
    let hashmap = {
        '[' : ']',
        '{' : '}',
        '(' : ')'
    }
    let stack = [];
    for (let char of s) {
        if (char in hashmap) {
            stack.push(char);
            continue;
        } else {
            if (stack.length === 0 || hashmap[stack.pop()] !== char) return false;
        }
    }
    return stack.length === 0;
};

// o(n)
// o(n)
