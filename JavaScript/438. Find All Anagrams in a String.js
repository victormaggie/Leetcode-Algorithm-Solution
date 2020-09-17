var findAnagrams = function(s, p) {
    let ans = [];
    let countS = Array(26).fill(0);
    let countP = Array(26).fill(0);
    const index = (p, num) => p.charCodeAt(num) - 'a'.charCodeAt(0);
    for (let i=0; i < p.length; i++) countP[index(p, i)]++;

    let start = 0;
    for (let i = 0; i < s.length; i++) {
        countS[index(s, i)]++;
        if (i > p.length-1) {
            countS[index(s, start)]--;
            start++;
        }
        if (JSON.stringify(countS) == JSON.stringify(countP)) ans.push(start);
    }
    return ans;
};

