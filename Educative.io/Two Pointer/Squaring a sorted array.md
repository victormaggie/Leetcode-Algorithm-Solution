
LC 977.

Given a sorted array, create a new array containing squares of all  the number of the input array.

`Input: [-2, -1, 0, 2, 3]`
`Output: [0, 1, 4, 4, 9]`

```
const make_squares = function(arr) {
    let squares = Array(arr.length);
    let left = 0, right = arr.length-1, m = right;
    while (left <= right) {
        const leftValue = arr[left] * arr[left];
        const rightValue = arr[right] * arr[right];
        if (leftValue > rightValue) {
            squares[m] = leftValue;
            left++;
        } else {
            squares[m] = rightValue;
            right--;
        }
        m --;
    }
    return squares;
}
```

