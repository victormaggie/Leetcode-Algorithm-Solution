
#### Problem statement 

Given an array of sorted numbers, remove all duplicates from it.

You should not use extra space after removing the duplicate in-place, return the length of the subarray in it.

```
const remove_duplicates = function(arr) {
    if (!arr) return 0;
    let fast = 1, slow = 0, cnt = 1;
    while (fast < arr.length) {
        if (arr[fast] != arr[slow]) {
            slow = fast;
            cnt ++;
        }
    }
    return cnt;
}

```


Similiar questions --> unsorted array here!

```
function remove_element(arr, key) {
    let j = 0;
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] != key) {
            arr[j] = arr[i];
            j ++
        }
    }
    return j;
}

```