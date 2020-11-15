
### Maximum Sum Subarray of Size K (easy)

Given an array of positive numbers and a positive number `K`, find the maximum sum of any contiguous subarray of size `K`.

#### Example 1

`Input : [2, 1, 5, 1, 3, 2], K = 3`
`Output : 9` 

- Brute-force solution
```
function max_sub_array_of_size_k(k, arr) {
    let maxSum = 0,
    windowSum = 0;
    for (let i = 0; i < arr.length - k + 1; i++){
        windowSum = 0;
        for (j = i; j < i + k; j++) {
            windowSum += arr[j];
        }
        maxSum = Math.max(maxSum, windowSum);
    }
    return maxSum;
}
```

- Sliding window solution
```
function max_sub_array_of_size_k(k, arr) {
    let sum = 0,
    ans = 0;
    for (let i = 0; i < arr.length; i++) {
        sum += arr[i];
        if (i >= k-1) {
            ans = Math.max(ans, sum);
            sum -= arr[i-k+1];
        }
    }
    return sum;
}
```

Time complexity `o(N)` solution
Space complexity `o(1)` solution

