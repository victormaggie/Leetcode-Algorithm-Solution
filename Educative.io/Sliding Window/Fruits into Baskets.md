#### Problem statement

`Given an array of characters where each character represents a fruit tree`. You are given two basket and your goal is to put `maximum number of fruits in each basket`. 

- constraint: each basket can only have one type of fruit.

```
const fruits_into_baskets = function(fruits) {
    let hashmap = {}, res = 0;
    for(let i = 0, j = 0; i < fruits.length; i++) {
        // open window here
        if (!hashmap[fruits[i]]) hashmap[fruits[i]] = 0;
        // close window here
        while (Object.keys(hashmap).length > 2) {
            hashmap[fruits[j]] --;
            if (hashmap[fruits[j]] == 0) delete hashmap[fruits[j]];
            j ++
        }
        res = Math.max(res, i - j + 1);
    }
    return res;
}

// use the sliding window solution.
// the same as the longest K distinct characters.

---

fixed sliding window!

```
