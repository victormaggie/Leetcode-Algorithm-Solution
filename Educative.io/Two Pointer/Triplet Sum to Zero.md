
Given an array of unsorted numbers, find all unique triplets in it and add up to zeros.

`Input: [-3, 0, 1, 2, -1, 1, -2]`
`Ouput: [-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]`

This is a two pointer solution

However two tips:

1. The array should be sorted.
2. In order to avoid the duplicate number we need get rid of the duplicate number



```
var threeSum = function(arr) {
    
  arr.sort((a, b) => a - b);
  let res = [];

  for (let i = 0; i < arr.length - 2; i++) {
    if (i && arr[i-1] == arr[i]) continue;
    let left = i + 1, right = arr.length-1, target = -arr[i];
    
    // [0, 0, 0] this is an edge case, cannot support here!
    if (arr[i] > 0) break;

    while (left < right) {
      sum = arr[left] + arr[right];
      if (sum === target) {
        res.push([arr[i], arr[left], arr[right]]);  
        // get rid of the duplicate one here
        while (left < right && arr[right-1] === arr[right]) right--;
        while (left < right && arr[left+1] === arr[left]) left++;
        right --;
        left ++;
      }

      else if (sum > target) right --;
      else left ++

    }
  }

  return res;
};


Time complexity o(n)
Space complexity o(1)

LC 15
```