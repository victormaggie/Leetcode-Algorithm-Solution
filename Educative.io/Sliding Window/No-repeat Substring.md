#### No-repeat Substring

- Problem statement
- String = 'aabccbb'
- output 3

---
Find the length of the longest substring, which has no repeating characters.

- The difference between the previous one is that we need to take care of the `freqency`! previous one take care of the `key`.

```
const non_repeat_substring = function(str) {
    // define hashmap here !
    let hashmap = {}, ans = 0;
    for (let i = 0, j = 0; i < str.length; i ++) {
        if (!hashmap[str[i]]) hashmap[str[i]] = 0;
        hashmap[str[i]] ++;

        while (hashmap[str[i]] > 1) {
            hashmap[str[j]] --;
            if (hashmap[str[j]] == 0) delete hashmap[str[j]];
            j ++;
        }
        ans = Math.max(ans, i - j + 1);
    }
    return ans;
}


```

- o (n) solution
- Dynamic sliding window here, whenever we get a repeating character, we will shrink our sliding window to ensure that we always have distinct characters in the sliding window.



```
const non_repeat_substring = function(str) {

    let hashmap = {}, ans = 0;
    for (let i = 0, j = 0; i < str.length; i++) {
        rightChar = str[i];
        if (rightChar in hashmap) {
            // jump away from the hashmap.
            j = Math.max(j, hashmap[rightChar] + 1)
        } 
        hashmap[rightChar] = i;
        ans = Math.max(ans, i - j + 1);
    }
    return ans;
}

```