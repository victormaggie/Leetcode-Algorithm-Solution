var partitionLabels = function(S) {

    let dict = {};

    for (let i = 0; i < S.length; i++) {
        
        if (!(S[i] in dict)) {
            dict[S[i]] = 0;
        }
        dict[S[i]] = i;
    }

    let index = 0;
    let start = 0;
    const ans = [];
    for (let i = 0; i < S.lenght; i++) {
        index = Math.max(dict[S[i], index]);
        if (i == index) {
            ans.push(i- start + 1);
            start = i + 1;
        }
    }
    return ans;
};

// gready solution
//