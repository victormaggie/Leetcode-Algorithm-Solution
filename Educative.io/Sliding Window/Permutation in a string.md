
#### Problem statement

Given a string and a pattern, find out if the string contains any permutation of the pattern.

`Permutation` 


```
var checkInclusion = function(str, pattern) {
    
    let hash = {}, cnt = 0, m = 0;

    // define the hashmap here
    for (let char of str) {
        if (!hash[char]) hash[char] = 0;
        hash[char] ++;
    }
    
    
    // sliding window solution
    for (let i = 0, j = 0; i < pattern.length; i ++) {
        
        if (pattern[i] in hash) {
            hash[pattern[i]] --;
            if (hash[pattern[i]] == 0) {
                cnt ++;
            }
        }
        
        if (cnt === Object.keys(hash).length) return true;
        
        // shrink the sliding window
        if (i >= str.length - 1) {
            // the last character
            if (pattern[j] in hash) {
                if (hash[pattern[j]] == 0) cnt--;
                hash[pattern[j]] ++;
            }
            j ++;   
        }
    }
    return false;
};

```

- if it is python code, it will be super easy!


```
function find_permutation(str, pattern) {
  let windowStart = 0,
    matched = 0,
    charFrequency = {};

  for (i = 0; i < pattern.length; i++) {
    const chr = pattern[i];
    if (!(chr in charFrequency)) {
      charFrequency[chr] = 0;
    }
    charFrequency[chr] += 1;
  }

  // Our goal is to match all the characters from the 'charFrequency' with the current window
  // try to extend the range [windowStart, windowEnd]
  for (windowEnd = 0; windowEnd < str.length; windowEnd++) {
    const rightChar = str[windowEnd];
    if (rightChar in charFrequency) {
      // Decrement the frequency of matched character
      charFrequency[rightChar] -= 1;
      if (charFrequency[rightChar] === 0) {
        matched += 1;
      }
    }

    if (matched === Object.keys(charFrequency).length) {
      return true;
    }

    // Shrink the sliding window
    if (windowEnd >= pattern.length - 1) {
      leftChar = str[windowStart];
      windowStart += 1;
      if (leftChar in charFrequency) {
        if (charFrequency[leftChar] === 0) {
          matched -= 1;
        }
        charFrequency[leftChar] += 1;
      }
    }
  }
  return false;
}

```