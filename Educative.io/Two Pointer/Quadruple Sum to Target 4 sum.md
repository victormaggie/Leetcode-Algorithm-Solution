
Problem statement

`Input: [4, 1, 2, -1, 1, -3], target = 1`
`Output: [-3, -1, 1, 4], [-3, 1, 1, 2]`

4 sum solution, 

we can first sort the array,
use 2 iterate and two pointer. time complexity o(n^3)


LC 18. 
```
const search_quadruplets = function(arr, target) {
  let res = [];

  arr.sort((a, b) => a - b);

  for (let i = 0; i < arr.length -3; i++) {
    if (i && arr[i-1] === arr[i]) continue;
    for (let j = i + 1; j < arr.length -2; j++){
      if (j != i+1 && arr[j-1] === arr[j]) continue;
      let left = j + 1, right = arr.length-1;
      while (left < right) {
        const totalSum = arr[i] + arr[j] + arr[left] + arr[right];
        if (totalSum === target) {
          res.push([arr[i], arr[j], arr[left], arr[right]]);
          while (left < right && arr[left+1] === arr[left] ) left++;
          while (left < right && arr[right-1] === arr[right]) right --;
          left ++;
          right --;
        } else if (totalSum > target) right--;
        else left++;
      }
    }
  }

  return res;
};


o ( n ^ 3) Solution !
```