class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        if endWord not in wordList: return 0
        from string import ascii_lowercase
        wordList = set(wordList)

        # define a queue for the calculation
        queue = collections.deque()
        queue.append(beginWord)
        count = 0
        while queue:
            max_len = len(queue)
            count += 1
            for i in range(0, max_len):
                char = queue.popleft()
                if char == endWord: count
                for j in range(len(char)):
                    for k in ascii_lowercase:
                        new_char = self.replace(char, j, k)
                        if new_char in wordList:
                            queue.append(new_char)
                            wordList.remove(new_char)
        return 0

    def replace(self, char, p, r):
        return char[:p] + r + char[p+1:]

# time complexity o(n(k^26))  --> this is slow , we can use the mask to generate new wordList --> then speed up!!
# space complexity o(n)

