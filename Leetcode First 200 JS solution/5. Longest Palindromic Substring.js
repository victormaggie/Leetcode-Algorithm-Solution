/* Given a string s,
return the longest palidromic substring s
*/

var longestPalindrome = function(s) {

    // use the center spread solution
    let ans = '';
    let strLength = s.length;

    for (let i = 0; i < strLength; i++) {
        str1 = isPalindrome(i-1, i+1);
        str2 = isPalindrome(i, i+1);
        const temp = str1.length > str2.length ? str1 : str2;
        ans = temp.length > ans.length ? temp : ans;
    }
    return ans;

    function isPalindrome(leftIndex, rightIndex) {
        while (leftIndex >= 0 && rightIndex < strLength && s[leftIndex] === s[rightIndex]) {
            leftIndex -= 1;
            rightIndex += 1;
        }
        return s.slice(leftIndex + 1, rightIndex);
    }
}

// o(n^2) time complexity 
// o(n) space complexity 

var longestPalindrome = function(s) {

    // use the center spread solution
    let ans = '';
    let strLength = s.length;
    let start = 0, end = 0

    for (let i = 0; i < s.length; i++) {
        let tempStart = i;
        let tempEnd = i;

        while (s[i] === s[tempEnd + 1]) tempEnd++;

        while (tempStart >= 0 && tempEnd < s.length && s[tempStart - 1] == s[tempEnd + 1]){
            tempStart -= 1;
            tempEnd   += 1;
        }

        if (max < tempEnd - tempStart + 1) {
            start = tempStart;
            end   = tempEnd;
            max   = tempEnd - tempStart + 1;
        }
    }
    return s.substring(start, end+1);
};

// o(n^2)
// o(1) solution


// solution 3 dynamic programming
