
#### Pair with target sum

Given an array of `sorted numbers` and a target sum, find a pair in the array whose sum is equal to the given target.

`Input : [1, 2, 3, 4, 5]`
`target : 6`
`explanation: `

```
function pair_with_target_sum(arr, target) {
    let left = 0, right = arr.length-1;
    while (left < right) {
        const sum = arr[left] + arr[right];
        if (target == sum){
            return [left, right];
        }

        if (target > sum) right --
        else left ++;
    }
    return [-1, -1]
}

```