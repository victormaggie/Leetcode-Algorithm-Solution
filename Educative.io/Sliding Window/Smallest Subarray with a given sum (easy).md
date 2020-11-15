#### Smallest subarray with a given sum (easy)

- `Input: [2, 1, 5, 2, 3, 2]`
- `Output: 2`
- `The smallest subarray with a sum great than or equal to 7 is [5, 2]`



#### Procedure for this question

- First, we will add-up elements from the beginning of the array `i` until their sum become greater than or equals to `S`.
- These element will consist our sliding window.
- We try to shrink the sliding window by the `j`, until the sum is smaller than `S`.
- memorize the smaller window size. 



```
const smallest_subarray_with_given_sum = function(s, arr) {
    let sum = 0, res = '0X7FFFFF';
    for (let i = 0, j = 0; i < arr.length; i++) {
        sum += arr[i];
        // here is the checking point
        while (sum >= s) {
            sum -= arr[j];
            res = Math.min(res, i - j + 1);
            j ++;
        }
    }
    return res === '0x7FFFFF` ? 0 : res;
}
```


The sliding window size is not fixed in this question.

Time complexity O(2N)
Space complexity o(1)
