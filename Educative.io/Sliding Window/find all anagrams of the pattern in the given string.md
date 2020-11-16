
#### Anagram is actually a permutation 

`Input: string = ppqp` , pattern = 'pq'

```
var findAnagrams = function(str, pattern) {
      result_indexes = [];
      // TODO: Write your code here
      let hash = {}, cnt = 0, m = 0, res = [];

      for (let char of pattern) {
        if (!hash[char]) hash[char] = 0;
        hash[char] ++;
        m ++;
      }

      for (let i = 0, j = 0; i < str.length; i++) {

        if (str[i] in hash) {
          hash[str[i]] --;
          if (hash[str[i]] === 0) cnt ++;
        }
        if (cnt === Object.keys(hash).length) res.push(j);

        if ( i >= m - 1 ) {
          if (str[j] in hash) {
            if (hash[str[j]] === 0) cnt --;
            hash[str[j]] ++;
          }
          j ++
        }
      }
      return res;
};

This question is the same as the permutation in a string as continuous substring.

--- 

Fixed sliding window -- > 


```

