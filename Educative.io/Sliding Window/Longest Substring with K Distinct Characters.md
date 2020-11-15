#### Problem statement

- Given a string, find the length of the `longest substring` in it with no more than K distinct characters.

`Input: String: 'araaci', K = 2`
`Output: 4`

```
const longest_substring_with_k_distinct = function(str, k) {
    let hashmap = {}, res = 0;
    for (let i = 0, j = 0; i < str.length; i++) {
        if (!hashmap[str[i]]) hashmap[str[i]] = 0;
        hashmap[str[i]] ++;

        while (Object.keys(hashmap).length > k) {
            hashmap[str[j]] --;
            if (hashmap[str[j]] == 0) delete hashmap[str[j]];
            j ++;
        }

        res = Math.max(res, i - j + 1)
    }
    return res;
}

```


#### Procedure
- Insert characters from the beginning of the string until we have 'K' distinct characters in the `Hashmap`
- These characters will constitute our sliding window. 
- Shrink the window when we have more than K characters in our `Hashmap`, decrease the character frequency at index `j`, and delete the `key` once its frequency equals `0`.
- At the end of each step, we will check the window length is the longest so far.


Time complexity : O(N)
Space complexity : O(K)
