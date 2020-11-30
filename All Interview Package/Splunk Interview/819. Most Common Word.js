var mostCommonWord = function(paragraph, banned) {
    
    words = paragraph.toLowerCase().split(/\W+/);
    
    let hashmap = {};
    
    for (let word of words) {
        if (!banned.includes(word)) {
            if (!(word in hashmap)) {
                hashmap[word] = 0;
            }
            hashmap[word] += 1;
        }
    }
    
    // sort the value
    let ans = '', count = 0;
    for (let key in hashmap) {
        if (hashmap[key] > count){
            ans = key;
            count = hashmap[key];
        }
    }
    
    return ans;
};

