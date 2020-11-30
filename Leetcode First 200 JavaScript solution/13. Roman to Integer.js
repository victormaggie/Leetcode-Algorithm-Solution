var romanToInt = function(s) {
    let hashmap = {
        'I': 1, 
        'V': 5,
        'X': 10,
        'L':50,
        'C':500,
        'D':500,
        'M':1000,
    }

    let ans = 0;
    for (let i = 0; i < s.length; i++) {
        if (i == 0 || hashmap[s[i]] <= hashmap[s[i-1]]) {
            ans += hashmap[s[i]];
        } else {
            const value = -hashmap[s[i-1]] * 2 + hashmap[s[i]];
            ans += value;
        }
    }
    return ans;
};

// o(n)

// or we can solve this one use two pointer !
