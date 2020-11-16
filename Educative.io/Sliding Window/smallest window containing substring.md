
Given a string and a pattern, find the smallest substring in the given string.
which has all the characters of the given pattern.


This is the dynamic sliding window questions. Followed by the Permutation, however the characters in sliding window
will be redundant

```
var minWindow = function(s, t) {

    // sliding window solution.
    let hash = {}, m =0 , cnt=0, minLength = Infinity, substart = 0;

    for (let char of t) {
        if (!hash[char]) hash[char] = 0;
        hash[char] ++;
        m ++;
    }

    for (let i = 0, j = 0; i < s.length; i++) {
        if (s[i] in hash) {
            hash[s[i]] --;
            // all the valid count
            if (hash[s[i]] >= 0) cnt++;
        }
        
        // if all the value are matched here
        // we try to shrink the sliding window

        while (cnt === m) {
            if (minLength > i - j + 1) {
                minLength = i - j + 1;
                substart = j;
            }
            // try to shrink
            if (s[j] in hash) {
                if (hash[s[j]] === 0) cnt --;
                hash[s[j]]++;
            }
            j++;
        }
    }

    return minLength !== Infinity ? s.substr(substart, minLength) : '';
}


// when matched all the character, then try to shrink the sliding window

```