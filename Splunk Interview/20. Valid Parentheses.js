var isValid = function(s) {
    
    hashmap = {
        '(' : ')',
        '{' : '}',
        '[' : ']',
    }

    let stack = [];
    for (let char of s) {
        
        if (char in hashmap) {
            stack.push(char)
        } else {
            if (stack && hashmap[stack.pop()] !== char) return false
        }
    }

    return stack.length === 0;
}

// o(n) hashmap solution
