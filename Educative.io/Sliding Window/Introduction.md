
### Sliding window

`Key words: Continuous subarray!` 

Given an array, find the average of all `contiguous subarrays` of size ‘K’ in it.

- Brute force solution will be `o(N x K)` time complexity
- Sliding window will have `o(N)` time complexity


#### Brute force solution
```
function find_averages_of_subarrays(K, arr) {
    const result = [];
    for (let i = 0; i < arr.length; i++) {
        sum = 0;
        for (let j = i; j < arr.length - K + 1; j++) {
            sum += arr[j];
        }
        result.push(sum / K);
    }
    return result;
}

```

---

#### Sliding window solution
```
function find_averages_of_subarrays(K, arr) {
    const result = [];
    let sum = 0;
    for (let i = 0; i < arr.length; i++) {
        if (i <= K - 1) {
            sum += arr[i];
            continue;
        }
    result.push(sum/K);
    sum += arr[i];
    sum -= arr[i - K];
    }
    return result;
}

```

- better solution

```
function find_averages_of_subarrays(K, arr) {
    const result = [];
    let sum = 0;
    for (let i = 0; i < arr.length; i++) {
        sum += arr[i];
        // only when the window is full then calculate
        if (i >= K - 1) {
            result.push(sum / K);
            sum -= arr[i - K + 1];
        }
    }
    retunr result;
}

```

This is fixed size sliding window solution. No need to calculate the window end, just use the starting point - K + 1 .
