
var groupAnagrams = function(strs){
    let map = new Map();

    for (str of strs){
        let key = 0;
        for (let char of str){
            const i = char.charCodeAt(0);
            key += Math.pow(i, 4);
        }
        !map.has(key)
            ? map.set(key, [str])
            : map.set(key, map.get(key).concat(str))
    }
};