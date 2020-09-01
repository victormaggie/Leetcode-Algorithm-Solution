var mostCommonWord = function(paragraph, banned) {
    let dict = {}
    paragraph = paragraph.toLowerCase().split(/\W+/);

    let ans = '';
    let count = 0;
    for (let i=0; i<paragraph.length; i++) {
        key = paragraph[i];
        if (dict[key] == null) dict[key] = 0;
        dict[key] += 1;
    }

    for (key in dict) {
        if((dict[key] > count) && !(banned.includes(key))) {
            ans = key;
            count = dict[key];
        }
    }
    return ans;
}

// time complexity o(n)
// space complexity o(n)
