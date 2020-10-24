var reconstructQueue = function(people) {
    
    const n = people.length;
    const ans = Array.from({length: n});
    people.sort((a, b) => {
        if (a[0] != b[0]) return a[0] - b[0];
        return b[1] - a[1];
    });
    
    for (let i = 0; i < n; i++) {
        let h = people[i][0], k = people[i][1];
        let j = 0, cnt = 0;
        while (cnt != k + 1)
            if (ans[j++] == undefined)
                cnt++;
        ans[j-1] = people[i]
    }
    return ans;
};

