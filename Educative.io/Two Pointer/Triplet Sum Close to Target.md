
Given an array of unsorted numbers and a target number, find a triplet in the array whose sum is as close to the target number as possible.

`Input: [-2, 0, 1, 2]`
`Target: 2`

Triplet [-2, 1, 2] has the closest sum to the target

```
const triplet_sum_close_to_target = function(arr, target_sum) {
    // Cannot get the smallest one, as such using memorization here
    let res = 0, memo = Infinity;
    arr.sort((a, b) => a-b);

    for (let i = 0; i < arr.length-2; i ++) {
        if (i && arr[i-1] === arr[i]) continue;
        
        // two pointer here
        left = i + 1, right = arr.length-1;
        while (left < right) {
        const total = arr[i] + arr[left] + arr[right];
        let difference = Math.abs(target_sum - total);
        if (difference < memo){
            memo = difference;
            res = total;
        }
        if (total > target_sum) right--;
        else if (total < target_sum) left++;
        else return target_sum;
        }
    }
  return res
};

```