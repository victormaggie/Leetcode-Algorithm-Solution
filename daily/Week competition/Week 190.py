from typing import List

# Question 1
class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        # edge case
        if not sentence: return -1
        if not searchWord: return 

        sentence = sentence.split(' ')
        # o(n)
        for idx, val in enumerate(sentence):
            if val.find(searchWord) == 0: # o(n)
                return idx + 1
        
        return -1

# time complexity o(n^2)
# space complexity o(n)


    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        if not sentence: return -1
        if not searchWord: return

        sentence = [x.group(0) for x in re.finditer(r"[a-z]+", sentence)]
        # I like use mapping, great function
        res = map(lambda x: x.startswith(searchWord), sentence)
        count = 0
        for i in res:
            count += 1
            if i == True: return count
        return -1

# because map function is high performance --> this algorithm is better than brute force


# Question 2:
# be aware of that use less max(a,b)
class Solution:
    def maxVowels(self, s: str, k: int) ->int:
        if not s or not k: return 0
        start, end = 0, 0
        res = 0
        # we do not need to store element
        queue = collections.deque()
        vowels = set({'a', 'e', 'i', 'o', 'u'})
        temp = 0
        for end in range(len(s)):
            if end < k:
                queue.append(s[end])
                if s[end] in vowels:
                    temp += 1
                    res = max(res, temp)
                    if res < temp: res = temp
                    return 
            
            # left = s[start]
            left = queue.popleft()
            right = s[end]
            # we do not need to store
            queue.append(right)
            if left in vowels and right in vowels:
                pass
            elif left in vowels:
                temp -= 1
            else: temp +=1 
            if res < temp: res = temp
            start += 1
        return res

# using set and if res < temp: can beat 100% 


    def maxVowels(self, s: str, k: int) -> int:
        res = j = vowels = 0
        for i, c in enumerate(s):
            vowels += c in 'aeiou'
            # very neat solution
            if i - j + 1 > k:
                vowels -= s[j] in 'aeiou'
                j += 1
            
            if i - j + 1 == k:
                res = max(res, vowels)
            return res

# Question 3: Psedo-palindromic path 

class Solution:
    def pseudoPalindromicPaths(self, root: TreeNode) -> int:
        if not root: return
        self.ans = 0
        self.dfs(root, [root.val])
        return self.ans
    
    def dfs(self, root, path):
        # check the leaf node
        if not root.left and not root.right:
            if len(path) <= 1:
                self.ans += 1
        return 
        if root.left:
            new_val = root.left.val
            if new_val in path:
                path.remove(new_val)
                self.dfs(root.left, path)
                path.append(new_val)
            else:
                path.append(new_val)
                self.dfs(root.left, path)
                path.remove(new_val)
            
        if root.right:
            new_val = root.right.val
            if new_val in path:
                path.
