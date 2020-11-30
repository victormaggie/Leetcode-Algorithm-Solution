var strStr = function(haystack, needle) {
    if (needle.length === 0) return 0;

    let i = 0;
    while (i < haystack.length) {
        let count = 0;
        let p = i;
        while (haystack[p] == needle[count] && count < needle.length) {
            p += 1;
            count ++
            if (count == needle.length) {
                return p - count;
            }  
        }
        i ++;
    }
    return -1;
};

// o(n*(n -l)) solution
// o(1)


//  should use KMP algorithm ..


