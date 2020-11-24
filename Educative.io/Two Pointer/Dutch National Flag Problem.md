
Given an array containing 0s, 1s and 2s, sort the array in-place

sort array that has 0, 1, 2

```
const sort = function (arr) {
    let low = 0, high = arr.length -1, i = 0;
    while (i <= high) {
        if (arr[i] === 0) {
            [arr[i], arr[low]] = [arr[low], arr[i]];
            low ++;
            i ++;
        } else if (arr[i] === 1) {
            i ++;
        } else {
            [arr[i], arr[high]] = [arr[high], arr[i]];
            high++;
        }
    }
    return arr;
}

```

o(n) time complexity.