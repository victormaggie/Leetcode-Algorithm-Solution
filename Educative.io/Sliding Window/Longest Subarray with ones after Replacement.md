
#### Problem statement

Given an array containing 0 and 1. if you are allowed to replace no more than `k` 0 with 1s, find the length of longest contiguous subarray having all 1s


`Input Array: [0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], k = 2`


```
const length_of_longest_substring = function(arr, k) {
    let ones = 0, res = 0;

    for (let i = 0, j = 0; i < arr.length; i++) {
        if (arr[i] === 1) ones++;

        if (i - j + 1 - ones > k) {
            if (arr[j++] === 1) ones --;
        }
        res = Math.max(res, i - j + 1);
    }
    return res;
}

// two pointer  solution. 
// o(n) time complexity
// o(1) space complexity
```

