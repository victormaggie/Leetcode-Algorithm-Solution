var lengthOfLongestSubstring = function(s) {
    // sliding window solution

    let dict = {};
    windowStart = 0;
    maxLength = 0;

    for (let windowEnd = 0; windowEnd < s.length; windowEnd++) {
        const char = s[windowEnd];
        dict[char] = (dict[char] || 0) + 1;
        while (dict[char] > 1) {
            const leftChar = s[windowStart];
            dict[leftChar]--;
            if (dict[leftChar] === 0) delete dict[leftChar];
            windowStart += 1;
        }
        maxLength = Math.max(maxLength, windowEnd - windowStart + 1);
    }
    return maxLength;
};

// time complexity o(n)
// space complexity o(n)

