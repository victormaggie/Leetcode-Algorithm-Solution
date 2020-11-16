LC 30

Input: String="catfoxcat", Words=["cat", "fox"]

Count the word
```
function find_word_concatenation(str, words) {

    if (words.length === 0 || words[0].length === 0) return [];

    wordFrequency = {};

    words.forEach((word) => {
        if (!(word in wordFrequency)) wordFrequency[word] = 0;
        wordFrequency[word] ++;
    });

    const resultIndex = [], wordsCount = words.length;
    wordLength = words[0].length;

    for (let i = 0; i < (str.length - wordsCount * wordLength) + 1; i++) {
        const wordsSeen = {};
        for ( j = 0; j < wordsCount; j++) {
            next_word_index = i + j * wordLength;
            word = str.substring(next_word_index, next_word_index + wordLength);
            
            // if word not in the wordFrequency list
            if (!(word in wordFrequency)) break;

            // add the word to the wordSeen map
            if (!(word in wordsSeen)){
                wordsSeen[word] = 0;
            }
            wordsSeen[word]++;

            // no need to process further if the word has higher frequency
            if (wordsSeen[word] > (wordFrequency[word] || 0)){
                break;
            }
            // store all the index we have
            if (j + 1 === wordsCount ){
                resultIndex.push(i);
            }
        }
    }
    return resultIndex;
}

```

--- 

New solution; use all the iterate number; 
```
var findSubstring = function (s, words) {

    // edge case 
    if (words.length == 0 || words[0].length == 0) return [];
    let wordLength = words[0].length, wordFrequency = {}, res = [], count = words.length;
    
    words.forEach((word) => {
        if (!wordFrequency[word]) wordFrequency[word] = 0;
        wordFrequency[word]++;
    })
    
    for (let i = 0; i < s.length - wordLength * count + 1; i++) {
        
        let hash = {};
        for (let j = 0; j < count; j++) {
            next_word_index = i + j * wordLength
            const word = s.substring(next_word_index, next_word_index + wordLength)

            if (!(word in wordFrequency)) break;
            
            // add the word to the wordSeen map
            if (!(word in hash)) hash[word] = 0;
            hash[word] ++;
            
            // no need to process further if the word value is larger than the index
            if (hash[word] > (wordFrequency[word] || 0)) break;
            
            if (j + 1 === count) res.push(i);
        }
    }
    return res;
};


```