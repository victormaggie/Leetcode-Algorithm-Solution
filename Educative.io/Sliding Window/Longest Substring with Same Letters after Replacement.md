
- Leetcode 424 
  
- 424 Longest Repeating Character Replacement

```
var characterReplacement = function(s, k) {
    let hashmap = {}, res = 0;
    let freq = 0;

    for (let i = 0, j = 0; i < s.length; i++) {

        if (!hashmap[s[i]]) hashmap[s[i]] = 0;
        hashmap[s[i]] ++;

        // find the most frequent one
        freq = Math.max(freq, hashmap[s[i]]);

        // if the number of the character that needs replacement
        // actually this is the extreme case, so we do not need to consider others.
        if (i - j - freq > k) {
            hashmap[s[j++]] --;
        }

        res = Math.max(res, i - j + 1);
    }
    return res;
}

```

- the important takeaway is that if the number inside the `i` and `j` that need replace must be less than `k`.