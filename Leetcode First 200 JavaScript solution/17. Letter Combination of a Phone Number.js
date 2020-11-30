/**
 * @param {string} digits
 * @return {string[]}
 */
var letterCombinations = function(digits) {
    
    const hashmap = {
        '0': '',
        '1': '',
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }
    
    if (!digits) return []

    let ans = [];
    dfs(digits, 0, '');
    return ans;
    
    function dfs(digits, idx, path) {
        
        if (idx == digits.length) {
            ans.push(path);
            return;   
        }
        for (let char of hashmap[digits[idx]]){
            dfs(digits, idx+1, path+char)
        }
    }
};